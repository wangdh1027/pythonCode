# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:44:09 2019
一个数组中不相容的两个子数组的最大和问题
@author: comnet
"""
def maxarr(arr):
    car = 0
    maxnum = arr[0]
    arr1 = []
    for i in arr:
        car +=i
        maxnum = max(car,maxnum)
        car = max(0,car)
        arr1.append(maxnum)
    car = 0
    maxnum = arr[-1]
    arr2 = []
    for i in range(len(arr)-1,-1,-1):
        car +=arr[i]
        maxnum = max(car,maxnum)
        car = max(0,car)
        arr2.append(maxnum)
    print(arr2)
    arr2.reverse()
    res = arr1[0]+arr2[1]
    for i in range(len(arr1)-1):
        res = max(res,arr1[i]+arr2[i+1])
    return res
        
arr = [3,2,-4,5,2,-6,3]
print(maxarr(arr))