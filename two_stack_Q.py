# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 23:53:24 2017

@author: mnshr
"""

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] #returns the last element value
        
    def pop(self):
        if not self.stack2: 
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() #returns the last element and deletes it
        
    def put(self, value):
        self.stack1.append(value) #adds the element to the stack list
        

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
