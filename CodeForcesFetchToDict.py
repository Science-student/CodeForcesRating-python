from time import sleep
import requests,sys
from alive_progress import alive_bar
no_of_users = int(sys.argv[1]) if len(sys.argv) > 1 else 500
no_of_users=int(input("Enter the number you want to get or leave blank for default:")) or 500
API_url="https://codeforces.com/api"
rating_dict=requests.get(f"{API_url}/user.ratedList?activeOnly=true&includeRetired=false").json()
if rating_dict["status"]!="OK":
    print("seems like codeforces is blocking request")
    exit()
sleep(2)
desired_result_dict={}
rating_dict=rating_dict['result']
print(rating_dict[no_of_users])
with alive_bar(no_of_users) as bar:
    for user in rating_dict[:no_of_users+1]:
        desired_result_dict[user['handle']]={}

        for key in ('country','rating','organization','maxRating','registrationTimeSeconds'):
            desired_result_dict[user['handle']][key]=user[key] if key in user else ''

        try:
            contest_list=requests.get(f"{API_url}/user.rating?handle={user['handle']}").json()
            if contest_list['status']!='OK':
                print('someone is pissed huh?')
                with open("dict.txt","w") as f:
                    f.write(str(desired_result_dict))
                exit()

            desired_result_dict[user['handle']]['contest_list']={}
            contest_list=contest_list['result']

            for contest in contest_list:
                desired_result_dict[user['handle']]['contest_list'][contest['contestId']]={}

                for  key in ('rank','oldRating','newRating'):
                    desired_result_dict[user['handle']]['contest_list'][contest['contestId']][key]=contest[key]
            no_of_users-=1
            print(f"ADDED {user['handle']},{no_of_users+1} more left")
            sleep(2)
        except:
            with open("dict.txt","w") as f:
                f.write(str(desired_result_dict))

            print(user['handle'],"might be incorrect")
            sleep(2)
        bar()

with open("dict.txt","w") as f:
    f.write(str(desired_result_dict))

