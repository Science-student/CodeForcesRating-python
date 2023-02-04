# CodeForcesRating-python
Usage:

1. run `CodeForcesFetchToDict.py`, this should create a `dict.txt`
2. run `DictToCSV.py`, this will  create `Ratings.csv`

NOTE:Codeforces atmost allows only 1 requests per 2 seconds even after that there can be cases in which codeforces tries to ratelimit i.e block from access the site in that case,  the script will show `<username> might be incorrect`. Incase, this happens frequently try to increase `sleep(2)` to `sleep(4)`.
