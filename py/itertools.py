# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 06:56:47 2017

@author: mnshr
"""
#https://www.hackerrank.com/challenges/iterables-and-iterators
a=input().strip()
b=input().strip()
c=input().strip()
from itertools import combinations
b1=b.split(' ')
#print (b1)
b2=''
for i in range(int(a)):
    b2+=(''.join(b1[i]))
#print(b2)
#for i in range(int(a)):
ans = list(combinations(b2, int(c)))
cnt=0
num=0
for x in ans:
    #print(''.join(x))
    cnt+=1
    #print(x)
    if 'a' in x:
        num+=1
        continue
        
print(num/cnt)

#https://www.hackerrank.com/challenges/compress-the-string
from itertools import groupby
S = map(int, input())

for key, group in groupby(S): #using group by
    #print (key, group)
    print ("(%d, %d)" %(len(list(group)), key), end=" "),

#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
from itertools import combinations_with_replacement

a, b = input().strip().split(' ')
#print (a, b)
b=int(b)
a=sorted(a)
#for i in range(len(a)):
ans=list(combinations_with_replacement(a, b))
#print (ans)
for x in ans:
    print(''.join(x))

#https://www.hackerrank.com/challenges/itertools-combinations
    a, b = input().strip().split(" ")
    b = int(b)
    a = sorted(a)
    for i in range(b):
        ans = list(combinations(a, i+1))
        for x in ans:
            print(''.join(x))
#Following doesn't work?
st=[x for x in input().strip().split(' ')]
k=int(st[1])

#print (pr_lst)
for cnt in range(k):
    pr_lst= list(combinations(st[0], cnt+1)) #get all combinations
    pr_lst=sorted(pr_lst) #sort the array objects
    print (pr_lst)
    for i in pr_lst:
        #print ("%c%c" %(i[0], i[1])) #fails a test case
        print (''.join(i))
            
#https://www.hackerrank.com/challenges/itertools-permutations
from itertools import permutations
st=[x for x in input().strip().split(' ')]
k=int(st[1])

pr_lst= list(permutations(st[0], k)) #get all permutations
pr_lst=sorted(pr_lst) #sort the array objects
#print (pr_lst)
for i in pr_lst:
    #print ("%c%c" %(i[0], i[1])) #fails a test case
    print (''.join(i))

#https://www.hackerrank.com/challenges/itertools-product
#Py 3 solution
from itertools import product
A = [int(x) for x in input().strip().split(" ")] #split on space
B = [int(x) for x in input().strip().split(" ")] #strip leading/trailing space
#convert to int
#assign to A/B lists
ans = list(product(A, B)) #use the cartesian productio fn
for x in ans:
    print(x, end=" ") #to use space instead of return between prints
