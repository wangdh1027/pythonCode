# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:03:03 2019
最大子数组累乘积
"""
def maxchegnji(arr):
    resmin = arr[0]
    resmax = arr[0]
    res = arr[0]
    maxend = 0
    minend = 0
    for i in range(1,len(arr)):
        maxend = resmax*arr[i]
        minend = resmin*arr[i]
        resmax = max(maxend,minend,arr[i])
        resmin = min(maxend,minend,arr[i])
        res = max(resmax,resmin,arr[i])
    return res
print(maxchegnji([0.2,0.5,2,3,0.5]))