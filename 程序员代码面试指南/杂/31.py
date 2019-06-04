# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:20:07 2019
32
@author: comnet
"""

class Node(object):
    def __init__(self,val,l=0,r=0):
        self.data = val
        self.left = l
        self.right = r

right = Node(3,Node(6,Node(12,),Node(13,)),Node(7,Node(14,),Node(15,)))
left = Node(2,Node(4,Node(8,),Node(9,)))
root = Node(1,left,right)
def sysout(root):
    zhan1 = []
    zhan2 = []
    print([root.data])
    if root.left:
        zhan1.append(root.left)
    if root.right:
        zhan1.append(root.right)
    while len(zhan1)!=0 or len(zhan2)!=0:
        res = []
        if len(zhan1)!=0:
            while len(zhan1)!=0:
                one = zhan1.pop()
                res.append(one.data)
                if one.right:
                    zhan2.append(one.right)
                if one.left:
                    zhan2.append(one.left)
        else:
            while len(zhan2)!=0:
                one = zhan2.pop()
                res.append(one.data)
                if one.left:
                    zhan1.append(one.left)
                if one.right:
                    zhan1.append(one.right)
        print(res)
        res = []       
sysout(root)