#Written to solve https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
def max(l):
    return sorted(set(l))[-2]

test = int(input())
l = [int(_) for _ in input().split()]
print (max(l))

