# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:03:17 2019

@author: comnet
"""
def findok(i,j,arr):
    for n in range(0,i):
        if arr[n]==j or abs(j-arr[n]) == abs(i-n):
            return False
    return True
#res=0
def nQueen(i,n,arr):
    res = 0
    if i==n:
        print(arr)
        res+=1
    for j in range(0,n):
        if findok(i,j,arr):
            arr[i] = j
            res += nQueen(i+1,n,arr)
    return res
n = 11
res = nQueen(0,n,[0]*n)  
print(res) 