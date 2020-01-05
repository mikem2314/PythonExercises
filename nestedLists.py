if __name__ == '__main__':
    n = int(input())
    grades = [[input(), float(input())] for _ in range(n)]
    second_highest = sorted(list(set([marks for name, marks in grades])))[1]
    print('\n'.join([a for a,b in sorted(grades) if b == second_highest]))