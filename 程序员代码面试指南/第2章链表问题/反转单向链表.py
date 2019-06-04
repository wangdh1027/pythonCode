# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:04:27 2019

@author: comnet
"""

class Node():
    def __init__(self,nextnode = None,val = None):
        self.nextnode = nextnode
        self.val = val
head = Node(Node(Node(Node(Node(Node(None,6),5),4),3),2),1)
#while 1:
#    print(head.val)
#    head = head.nextnode
#    if not head:
#        break
tmp1 = None
tmp2 = None
while head:
    tmp2 = head.nextnode
    head.nextnode = tmp1
    tmp1 = head
    head = tmp2
head = tmp1
while head:
    print(head.val)
    head = head.nextnode
    