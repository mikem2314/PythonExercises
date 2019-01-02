import re

m = input("Please enter string: ")

matches = re.findall(r"[^aiueo]([aiueoAIUEO]{2,})(?=[^aiueo])", m)

if matches:
    for x in matches:
        print (x)
else:
    print ("-1")
