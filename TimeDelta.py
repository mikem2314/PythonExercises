#Written to solve https://www.hackerrank.com/challenges/python-time-delta/problem


import datetime

formatString = "%a %d %b %Y %H:%M:%S %z"
testCases = int(input())

for t in range(testCases):
    t1 = str(input())
    t2 = str(input())
    formatT1 = datetime.datetime.strptime(t1, formatString)
    formatT2 = datetime.datetime.strptime(t2, formatString)
    print (formatT1)
    print (formatT2)
    diff = formatT2 - formatT1

    print (int(abs(diff.total_seconds())))