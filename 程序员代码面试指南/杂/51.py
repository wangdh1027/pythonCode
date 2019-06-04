# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:18:51 2019
归并排序
@author: comnet
"""
def twolist(a1,a2):
    res = []
    while len(a1)!=0 and len(a2)!=0:
        res += [a1.pop()] if a1[-1]>a2[-1] else [a2.pop()]
    res += a2 if len(a1) == 0 else a1
    return res
def guibing(a):
    res = twolist(guibing(a[0:int(len(a)/2)]),guibing(a[int(len(a)/2):len(a)])) if len(a)>1 else a
    return res[::-1] 
print(twolist([-1,0,1,4,7],[2,5,8]))   
print(guibing([1,2,4,13,455,2,1,54,-4,-2,43,-234,-2342,123432]))
