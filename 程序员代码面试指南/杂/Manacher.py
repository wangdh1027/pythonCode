# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:16:50 2019

@author: comnet
"""
def Manacher(arr):
    if len(arr) ==0:
        return 0
    arr0 = '*'
    for i in arr:
        arr0 += i+'*'
    pArr = [0]*len(arr0)
    index = -1
    pR = -1
    Max = 0
    for i in range(len(arr0)): 
        pArr[i] = min(pArr[2 * index - i], pR - i) if pR > i else 1
        while i + pArr[i] < len(arr0) and i - pArr[i] > -1:
            if (arr0[i + pArr[i]] == arr0[i - pArr[i]]):
                pArr[i]+=1
            else:
                break
        if (i + pArr[i] > pR):
            pR = i + pArr[i]
            index = i
        Max = max(Max, pArr[i]);
    return Max - 1;
print(Manacher('acdsaaasdcadb'))
