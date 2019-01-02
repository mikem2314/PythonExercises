#Written to solve https://www.hackerrank.com/challenges/python-mutations/problem


s = input("Please enter a string: ")
t = input("Please enter an index and char to split on, separated by a space: ")

index = int(t[0])
char = t[2]

l = list(s)
l[index] = char
s = ''.join(l)

print (s)