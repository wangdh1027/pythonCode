# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:34:32 2019

@author: comnet
"""
class Node(object):
    def __init__(self,val,l=0,r=0):
        self.data = val
        self.left = l
        self.right = r
right = Node(14,Node(12),Node(16))
left = Node(6,Node(4),Node(8))
root = Node(10,left,right)
def treeTolist(root):
    if root.left:
        headleft,lostleft = treeTolist(root.left) 
        root.left,lostleft.right= lostleft,root
    else:
        headleft,lostleft =root,root   
    if root.right:
        headright,lostright = treeTolist(root.right) 
        root.right,headright.left = headright,root
    else:
        headright,lostright = root,root
    return headleft,lostright
head,lost = treeTolist(root)
