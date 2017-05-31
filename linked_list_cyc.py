# -*- coding: utf-8 -*-
"""
Created on Tue May 30 23:01:28 2017

@author: mnshr
"""

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head == None:
        return False
    
    tmp=head
    seen = []
    while tmp!= None:
        if tmp in seen:
            return True
        
        seen.append(tmp)
        tmp=tmp.next
    
    return False