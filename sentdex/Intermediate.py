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