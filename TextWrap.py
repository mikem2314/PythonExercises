#Written to solve https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

s = input()
t = input()

print (textwrap.fill(s,int(t)))