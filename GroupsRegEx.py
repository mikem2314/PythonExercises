#Written to solve https://www.hackerrank.com/challenges/re-group-groups/problem
import re

s = input("Enter string: ")

m = re.search(r'([a-zA-Z0-9])\1', s)

if m:
    print (m.group(1))
else:
    print ("-1")