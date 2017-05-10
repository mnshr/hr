# -*- coding: utf-8 -*-
"""
Created on Tue May 09 20:03:04 2017

@author: mnshr
"""

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def check_bst(node, lval, rval):
    if not node:
        return True
    if (lval and (node.data <= lval)) or (rval and (node.data>= rval)):
        return False
    if (not check_bst(node.left, lval, node.data) or not check_bst(node.right, node.data, rval)):
        return False
    return True

def check_binary_search_tree_(root):
  return check_bst(root, None, None)