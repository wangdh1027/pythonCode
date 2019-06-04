# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:54:44 2019
二叉树的四种遍历方式
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

def res(head):
    if head.lift:
        res(head.lift)
        print(head.data)
    else:
        print(head.data)
#res(a)


def digui(head):
    if head.lift:
        digui(head.lift)
    if head.right:
        digui(head.right)
    print(head.data)
digui(a)
def kuandu(head):
    print(head.data)
    stack = [head]
    while stack != []:
        one = stack[0]
        del(stack[0])
        if one.lift:
            print(one.lift.data)
            stack.append(one.lift)
        if one.right:
            print(one.right.data)
            stack.append(one.right)        

#def preOrder(root):
#    if not root:
#        return []
#    stack = [root]
#    res = []
#    while stack:
#        root = stack.pop()
#        res.append(root.data)
#        if root.right:
#            stack.append(root.right)
#        if root.lift:
#            stack.append(root.lift)
#    return res
def inOrder(root):
    if not root:
        return []
    stack = []
    res = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.lift
        if stack:                
            root = stack.pop()
            res.append(root.data)
            root = root.right
    return res
def perOrder(root):
    if not root:
        return []
    stack = []
    res = []
    while stack or root:
        while root:
            stack.append(root)
            res.append(root.data)
            root = root.lift
        if stack:
            root = stack.pop()
            root = root.right
    return res      
def postOrder(root):
    if not root:
        return []
    stack = []
    res = []
    while stack or root:
        while root:
            stack.append(root)
            res.append(root.data)
            root = root.right
        if stack:
            root = stack.pop()
            root = root.lift
    return res[::-1]
def postorder(root):
    if not root:
        return[]
    stack = []
    res = []
    while stack or root:
        while root:
            stack.append(root)
            res.append(root.data)
            root = root.right
        if stack:
            root = stack.pop()
            root = root.lift
    return res[::-1]
#print(postorder(a))






























