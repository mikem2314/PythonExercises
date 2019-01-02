S = input()

defResults = [False, False, False, False, False]

B = [(s.isalnum(), s.isalpha(), s.isdigit(), s.islower(), s.isupper()) for s in S]

for b in B:
    for i in range(0, 5):
        defResults[i] |= b[i]

for i in range(0, 5):
    print (defResults[i])