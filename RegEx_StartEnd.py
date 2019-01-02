#Written to solve https://www.hackerrank.com/challenges/re-start-re-end/problem
import re

s = input("Please enter string: ")
t = input("Please enter substring: ")


m = re.finditer(r'(?=(' + t + '))', s)

matched = False
for x in m:
    matched = True
    print ((x.start(1), x.end(1) - 1))

if matched == False:
    print ("(-1, -1)")