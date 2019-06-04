# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:48:25 2019
最大子数组问题
@author: comnet
"""
def maxarr(arr):
    car = 0
    maxnum = arr[0]
    for i in arr:
        car +=i
        maxnum = max(car,maxnum)
        car = max(0,car)
    return maxnum
def maxsonarr(arr):
    sum1 = -abs(arr[0])
    res = arr[0]
    for i in arr:
        sum1 = (max(sum1+i,i))
        res = max(res,sum1)
    return res
arr = [-3,-2,-4,5,-2,-5,-1,-3]
print(maxarr(arr))
print(maxsonarr(arr))