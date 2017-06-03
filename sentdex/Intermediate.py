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
 print(list(xyz))
 
 xyz = [i for i in input_list if div_by_five(i)]
 print(xyz)
 [i for i in range(5)]
 
#Range of 3 elements, 5 times in the outer loop
#simpler form of nested loop
[[ii for ii in range(3)] for i in range(5)]

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
    
#%%
#Using Enumerate
example = ['left','right','up','down']
# for i in range(len(example)):       #Enumerate is a better alternative
#     print(i, example[i])

for i,j in enumerate(example):
    print(i,j)

#Enumerate on Dict
example_dict = {'left':'<','right':'>','up':'^','down':'v',}
#[print(i,j) for i,j in enumerate(example_dict)]

new_dict = dict(enumerate(example_dict))
print (example_dict)
print (new_dict) #Prints the indexes

#%%

#Using zip to combine elements in 2 lists with common indexes
x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']

for a,b in zip(x,y):
    print(a,b)
    
for a,b,c in zip(x,y,z):
     print(a,b,c)

#Creates a list of tuples     
print(zip(x,y,z))
#Same as above
print(list(zip(x,y,z)))

#With 2 values we can convert it to a Dict
print(dict(zip(x,y)))

#Using list comprehension
[(a,b,c) for (a,b,c) in zip(x,y,z)]

#%%
import timeit
#Generators yield instead of return
def simple_gen():
    yield 'Oh'
    yield 'hello'
    yield 'there'
     
for i in simple_gen():
    print(i)

#Generator Expr using Generator function
print (i for i in simple_gen())
#List comprehension using Generator function
print [i for i in simple_gen()]

CORRECT_COMBO = (3, 6, 1)
found_c=False
def lets_find_combo():
    for c1 in range(10):
    #    if found_c:
    #        break
        for c2 in range(10):
    #        if found_c:
    #            break
            for c3 in range(10):
                if (c1, c2, c3) == CORRECT_COMBO:
                   print('Found the combo:{}'.format((c1, c2, c3)))
                   found_c = True
                   break
    #            print (c1, c2, c3) #Goes through all the combos of c1, c2 ,c3
                                  #if we didn't use break in all the loops
                              
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

def lets_use_gen():
    for (c1, c2, c3) in combo_gen(): #generators yields tuples in a stream
        #print(c1, c2, c3)
        if (c1, c2, c3) == CORRECT_COMBO:
            print('Found the combo:{}'.format((c1, c2, c3)))
            break

print timeit.timeit()
lets_use_gen()
print timeit.timeit()
lets_find_combo()
print timeit.timeit()

#%%