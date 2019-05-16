# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:50:54 2019
一个数组 两个数出现奇数次  其余的出现偶数次  求出现奇数次的两个数
@author: comnet
"""

def twoOdd(arr):
    e = 0
    e1 = 0
    for i in arr:
        e ^= i
    rightOne = e & (~e +1)
    for i in arr:
        if i & rightOne != 0:
            e1 ^= i    
    return e1,e^e1
print(twoOdd([1,2,3,4,4,3,3,2,1,6]))