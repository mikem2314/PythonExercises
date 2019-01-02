#Written to solve https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen

import re

s = input()
t = input()

matches = re.findall(r'(?=(' + t + '))', s)

print (int(len(matches)))