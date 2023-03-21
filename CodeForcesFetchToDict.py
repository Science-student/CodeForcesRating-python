from time import sleep
import requests
no_of_users=500
API_url="https://codeforces.com/api"
rating_dict=requests.get(f"{API_url}/user.ratedList?activeOnly=true&includeRetired=false").json()
if rating_dict["status"]!="OK":
    print("seems like codeforces is blocking request")
    exit()
sleep(2)
desired_result_dict={}
rating_dict=rating_dict['result']
print(rating_dict[no_of_users])

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

        print(f"ADDED {user['handle']}")
        sleep(2)

    except:
        with open("dict.txt","w") as f:
            f.write(str(desired_result_dict))

        print(user['handle'],"might be incorrect")
        sleep(2)

with open("dict.txt","w") as f:
    f.write(str(desired_result_dict))
