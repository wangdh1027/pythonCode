# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:07:41 2019
树的子结构
@author: comnet
"""

class Node(object):
    def __init__(self,val,l=0,r=0):
        self.data = val
        self.lift = l
        self.right = r
d = Node(4)
e = Node(8)
f = Node(12)
g = Node(16)
b = Node(6,d,e)
c = Node(14,f,g)
a = Node(10,b,c)
def sona(root,son):
    if son == 0:
        return True
    elif root == 0:
        return False
    elif root.data == son.data:
        return sona(root.lift,son.lift)&sona(root.right,son.right)
    else:
        return False
         
def bianli(root,son):
    res = False
    if root.data == son.data:
        res =sona(root,son)
    if (not res) and root.lift:
        res = bianli(root.lift,son)
    if (not res) and root.right:
        res =bianli(root.right,son) 
    return res
q = Node(10,Node(6))
print(bianli(a,q))