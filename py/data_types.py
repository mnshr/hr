# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 19:07:08 2017

@author: mnshr
"""
#https://www.hackerrank.com/challenges/finding-the-percentage
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    sum=0.00
    for i in range(len(student_marks[query_name])):
        sum=sum+student_marks[query_name][i]
    print '{0:.2f}'.format(sum/len(student_marks[query_name]))
    
#https://www.hackerrank.com/challenges/nested-list
max=100
max2=100
max_n=''
max_n2=''
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    if score<max:
        max2=max
        max_n2=max_n
        max=score
        max_n=name
    elif score<max2 and score>=max:
        max2=score
        max_n2=name

print max_n2
#-----------------------------------------------------------
a= [[raw_input(),float(raw_input())] for x in xrange(int(raw_input()))]
b = sorted(set(x[1] for x in a))
for name in sorted(x[0] for x in a if b[1]==x[1]):
  print name
    
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    max=-100
    max2=-100
    for i in range(n):
        if i==0:
            max=arr[i]
        elif arr[i]>max:
            max2=max
            max=arr[i]
        elif arr[i]>max2:
            if arr[i]==max:
                continue
            max2=arr[i]
    print max2    

    
#https://www.hackerrank.com/challenges/list-comprehensions
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    result=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k)!=n:
                    arr=[]
                    arr.append(i)
                    arr.append(j)
                    arr.append(k)
                    result.append(arr)
                    

#https://www.hackerrank.com/challenges/python-tuples            
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tpl=tuple(integer_list)
    print hash(tpl)
    
#https://www.hackerrank.com/challenges/python-lists
if __name__ == '__main__':
    N = int(raw_input())
    ls=[]
    for i in range(N):
        cmd=str(raw_input())
        cmd1=cmd.split()
        if cmd1[0]=='insert':
            pos=int(cmd1[1])
            val=int(cmd1[2])
            ls.insert(pos, val)
        elif cmd1[0]=='print':
            print ls
        elif cmd1[0]=='remove':
            val=int(cmd1[1])
            ls.remove(val)
        elif cmd1[0]=='append':
            val=int(cmd1[1])
            ls.append(val)
        elif cmd1[0]=='sort':
            ls.sort()
        elif cmd1[0]=='pop':
            ls.pop()
        elif cmd1[0]=='reverse':
            ls.reverse()

