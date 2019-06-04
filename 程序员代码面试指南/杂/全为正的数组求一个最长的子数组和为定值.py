# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:38:41 2019
全为正的数组，求一个最长的子数组，这个字数组的和为定值 sum


左右两个指针  滑动窗口
若窗口内和小于sum 则窗口友指针向右滑  窗口变大  因为以L开头在子数组已经不可能 和为sum
若窗口内和大于sum 则窗口左指针向右滑  窗口变小
若窗口内和等于sum 则窗口变大变小都行
@author: comnet
"""
def maxlong(arr,su):
    L = 0
    R = 0
    s = arr[0]
    res = 0
    while R<len(arr)-1:
        if s==su:
            res = max(res,R-L+1)
            s-=arr[L]
            L+=1
        elif s>su:
            s-=arr[L]
            L+=1
        else:
            R+=1
            if R==len(arr):
                break
            s+=arr[R]
    return res
print(maxlong([1,3,6,8,6,4,1,1,1,1,1,1,1,3],7))


