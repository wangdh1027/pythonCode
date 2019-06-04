# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:05:08 2019

@author: comnet
"""

def number(arr):
    res = True
    i = 0
    if arr[0]=='+' or arr[0]=='-':
        i = 1
    for n in range(i,len(arr)):
        if (arr[n] not in aaa+['e','E','.']):
            res = False
            break;
        if arr[n] == '.':
            for a in range(n,len(arr)):
                if (arr[n] not in aaa+['e','E']):
                    res = False
                    break
                if arr[n] in ['e','E']:
                    j = 0
                    if arr[n+1]=='+' or arr[n+1]=='-':
                        j = 1
                    for m in range(n+j,len(arr)):
                        if (arr[n] not in aaa):
                            res = False
                            break;
        if arr[n] in ['e','E']:
            j = 0
            if arr[n+1]=='+' or arr[n+1]=='-':
                j = 1
            for m in range(n+j,len(arr)):
                if (arr[n] not in aaa):
                    res = False
                    break;
        if not res:
            break
    return res
#print(number(list('123523412E2')))
class Node(object):
    def __init__(self,val,l=0):
        self.data = val
        self.next = l
def k(root,n):
    if root.next:
        res = k(root.next,n)
        if res[1]:
            return res
        elif res[0]==(n-1):
            return root.data,True
        else:
            return res[0]+1,False
    elif n==1:
        return root.data,True
    else:
        return 1,False

def reserve(root,nextnode):
    if nextnode.next:
        res = reserve(nextnode,nextnode.next)
        nextnode.next = root
        root.next = 0
        return res
    else:
        nextnode.next = root
        return nextnode
    
    
    
    
    
    
#root =  Node(1,Node(2,))
#print(k(root,1))
#aaa=reserve(root,root.next)



































