# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:10:58 2019

@author: comnet
"""


def digui(arr,k,n,i):
    if n == 0:
        return 1
    res = 0
    for j in arr[i]:
        res+=digui(arr,k,n-1,j)
    return res%1000000007

k = 1234
n =2
arr = [[i for i in range(1,k+1)]]
for i in range(1,k+1):
    nsum = []
    for j in range(1,i):
        if i%j!=0:
            nsum.append(j)
    for j in range(i,k+1):
        nsum.append(j)
    arr.append(nsum)
print(digui(arr,k,n,0))