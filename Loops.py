#Written to solve https://www.hackerrank.com/challenges/python-loops/problem

import sys

numInput = int(input("Enter integer: "))

if numInput < 0:
    raise ValueError("Non-negative integers only.")

for x in range(numInput):
    print (pow(x,2))