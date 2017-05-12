# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:48:56 2017

@author: mnshr
"""

def is_matched(expression):
    stack = []
    pairs = {"(": ")", "{": "}", "[": "]"}

    for c in expression:
        if c in pairs:
            stack.append(pairs[c])
        elif not stack or c != stack.pop():
            return False

    return not stack

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"