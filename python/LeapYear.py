'''Leap year finder
Description
Leap years occur according to the following formula: a leap year is divisible by four, but not by one hundred, unless
it is divisible by four hundred. For example, 1992, 1996, and 2000 are leap years, but 1993 and 1900 are not. The next
leap year that falls on a century will be 2400.
Input
Your program should take a year as input.
Output
Your program should print whether the year is or is not a leap year.'''

year=int(raw_input("What year : "))

if (year%4==0) :
    if(year%100==0) :
        if(year%400==0) :
            print "%d is leap year" % year
        else :
            print "%d is not leap year" % year
    else :
        print "%d is leap year" % year
else :
    print "%d is not leap year" % year

