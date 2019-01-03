#Written to solve https://www.hackerrank.com/challenges/python-time-delta/problem



import arrow

time = "Sun 10 May 2015 13:54:36 -07:00"
testTime = arrow.get(time, 'ddd D MMMM YYYY HH:mm:ss Z')

print(testTime)