import sys


def is_leap(year):
    leap = False
    
    if (year % 4 == 0) and (year % 100 != 0):
        print ("{0} is a leap year".format(year))
        leap = True
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        print ("{0} is a leap year".format(year))
        leap = True
    else:
        print ("{0} is not a leap year".format(year))

    return leap


year = int(input("Enter year to be checked: "))
is_leap(year)