# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 16:55:08 2017

@author: mnshr
"""
from __future__ import division 
from __future__ import print_function

#https://www.hackerrank.com/challenges/python-print
if __name__ == '__main__':
    n = int(raw_input())
    ar=[]
    for j in range(n+1):
        if j==0:
            continue
        ar.append(j)
    print(*ar, sep='') #using the print_function

#https://www.hackerrank.com/challenges/write-a-function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap=True
                return leap
            leap=False
            return leap
        leap=True
    return leap

#year = int(raw_input())
#print is_leap(year)

#https://www.hackerrank.com/challenges/python-loops
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        print i*i

#https://www.hackerrank.com/challenges/python-division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print a//b          #prints the integer part only
    print a/b           #prints the float
    
#https://www.hackerrank.com/challenges/py-if-else
if __name__ == '__main__':
    n = int(raw_input())
    if n % 2 != 0:
        print 'Weird'
    else:
        if 2<=n and n<=5:
            print 'Not Weird'
        elif n<=20 and n>=6:
            print 'Weird'
        elif n>20:
            print 'Not Weird'
            

#https://www.hackerrank.com/challenges/python-arithmetic-operators
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print a+b
    print a-b
    print a*b