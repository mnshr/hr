# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:30:56 2017

@author: mnshr
"""

# names = ['Jeff', 'Gary', 'Jill', 'Samantha']

# for name in names:
    #print('Hello there, ' + name)
    #print(' '.join(['Hello there', name]))
    
# print(', '.join(names))

# import os 
# 
# location_of_files = '/home/ubuntu/workspace/project/learning/python3-intermediate-tutorial/src'
# file_name = 'example.txt'
# 
# print(location_of_files + '/' + file_name)
# 
# with open(os.path.join(location_of_files, file_name)) as f:
#     print(f.read())

who = 'Gary'
how_many = 12

print(who, 'bought', how_many, 'apples today!')
print('{} bought {} apples today!'.format(who, how_many))

#%%
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? Can choose add, sub, mul, or div')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
    main()
    
#%%
# Generator vs List Comprehension
xyz = (i for i in range(50000000))
print(list(xyz)[:5])

# list comprehension puts the entire list into memory, so it is faster, 
# but the penalty is memory use
xyz = [i for i in range(50000000)]
print(xyz[:5])

#%%
 input_list = [5,6,2,1,6,7,10,12]
 
 def div_by_five(num):
     if num % 5 == 0:
         return True
     else:
         return False
 
 xyz = (i for i in input_list if div_by_five(i))
# print(list(xyz))
 
# xyz = [i for i in input_list if div_by_five(i)]
# print(xyz)
# [print (i) for i in range(5)]

[[print(i,ii) for ii in range(3)] for i in range(5)]

#%%
#generator
 input_list = range(100)
 
 def div_by_five(num):
     if num % 5 == 0:
         return True
     else:
         return False
  
 xyz = list(i for i in input_list if div_by_five(i))
 print xyz
 
 xyz_lc = [i for i in input_list if div_by_five(i)]
 print xyz_lc
 
import timeit
print(timeit.timeit('1+3', number=500000))

# ----------------------------------------------------- 100 items
# 1.21198258894
 print(timeit.timeit('''
 input_list = range(100)
  
 def div_by_five(num):
     if num % 5 == 0:
         return True
     else:
         return False
  
 xyz = list(i for i in input_list if div_by_five(i))
     ''', number=50000))

# 1.11570975033
 print(timeit.timeit('''
 input_list = range(100)

 def div_by_five(num):
     if num % 5 == 0:
         return True
     else:
         return False

 xyz = [i for i in input_list if div_by_five(i)]
 ''', number=50000))
#%%     
#Random list experiment
x=[1,2, 4, 7, 2, 5, 6]
# y=('a') This is a tuple, can't append to this
y=[] #This is a list element, we can append
print x[-1]
for i in range(len(x)):
    print i
    y.append(x[i])

print y[0], y[len(y)-1], y[-1] #the -1 index returns last element
y.pop()
print y

z=['abc', '123', 1, 5] #We can have different data type elements in a list
for i in range(len(z)):
    print z[i]