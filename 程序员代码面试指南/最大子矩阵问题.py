# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:41:27 2019
最大子矩阵问题
@author: comnet
"""
import sys
def maxarr(arr):
    car = 0
    maxnum = -sys.maxsize-1
    for i in arr:
        car +=i
        maxnum = car if car > maxnum else maxnum
        car = 0 if 0>car else car
    return maxnum
def maxsonarr(arr):
    res = -sys.maxsize-1
    for i in range(len(arr)):
        arrtmp = [0]*len(arr[0])
        for j in range(i,len(arr)):
            arrtmp = [arrtmp[n]+arr[j][n] for n in range(len(arrtmp))]
            tmp = maxarr(arrtmp)
            res = res if res > tmp else tmp
    return res
arr = [[3,2,-1],[-1,4,-3],[6,-5,9]]
print(maxsonarr(arr))
