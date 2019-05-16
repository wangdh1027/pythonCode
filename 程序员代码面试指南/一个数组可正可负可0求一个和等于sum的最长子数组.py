# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:25:47 2019

考虑以每个字符结束的子串

一个数组可正  可负 可0   求一个和  等于sum的最长子数组
变形：
一个数组中奇数个数和偶数个数相等的最长子数组：
奇数 ：-1 偶数：1  求和为0的最长自数组
@author: comnet
"""



def maxlen(arr,n):
    Map = {0:-1}
    res = 0 
    su = 0
    for i,val in enumerate(arr):
        su += val
        if (su-n) in Map:
            res = max(res,i-Map.get(su-n))
        if su not in Map:
            Map[su] = i
    print(res,Map)
maxlen([4,1,2,3,5,-3,8,9,2],-3)

#a = ['a/n/r000001',2,34,5,6,7,89,4,3,613,1238,23,]
#a.sort(key = lambda i:len(str(i)))
#print(a)
#your_data =  1# plug your awesome dataset here
#model = SuperCrossValidator(SuperDuper.fit, your_data, ResNet50, SGDOptimizer)# conquer world here


