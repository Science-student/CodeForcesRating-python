from  csv import  writer
from time import sleep
RatingDict=eval(open('dict.txt').read().strip())
with open('Rating.csv',"w") as csvfile:
    initial_row=['handle','country','rating','organization','maxRating','registrationTimeSeconds']
    csvwriter=writer(csvfile)
    csvwriter.writerow(initial_row+list(range(1,1972)))
    for i in RatingDict:
        if 'contest_list' not in RatingDict[i]:
            print(i,"does not seem to have contestlist maybe api blocked it")
        else:
            row=[RatingDict[i][key] if key !='handle' else i for key in initial_row]
            
            rating_change_list=[0]*1972
            for index in range(1,1973):
                Dict=RatingDict[i]['contest_list']
                rating_change_list[index-1]=Dict[index]['newRating']-Dict[index]['oldRating'] if index in Dict else '' 
            csvwriter.writerow(row+rating_change_list)

