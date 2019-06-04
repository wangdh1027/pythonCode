# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:53:23 2019

@author: comnet
"""

def find_n(n):
    a=2
    if n<10:
        return n
    n-=10
    x=10
    while 1:
        x = pow(10,a-1)*9*a
        print(n,x)
        if n<x:
            break
        n-=x
        a+=1
    i,j=int(n/a)+1,n%a
    return int(str(i)[j])
print(find_n(1001))
