# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:34:12 2019

@author: comnet
"""

"""
二分查找
"""
def binary_search(lis, num):
        left = 0
        right = len(lis) - 1
        while left <= right:   #循环条件
            mid = (left + right) // 2   #获取中间位置，数字的索引（序列前提是有序的）
            if num < lis[mid]:  #如果查询数字比中间数字小，那就去二分后的左边找，
                right = mid - 1   #来到左边后，需要将右变的边界换为mid-1
            elif num > lis[mid]:   #如果查询数字比中间数字大，那么去二分后的右边找
                left = mid + 1    #来到右边后，需要将左边的边界换为mid+1
            else:
                return mid  #如果查询数字刚好为中间值，返回该值得索引
        return -1  #如果循环结束，左边大于了右边，代表没有找到
def halfFid(lis,n):
    i = 0
    j = len(lis)
    while i<=j:
        half = (i+j)>>2
        if lis[half]==n:
            return half
        if lis[half]>n:
            j=half-1
        if lis[half]<n:
            i=half+1
    return -1
lis = [11, 32, 51, 21, 42, 9, 5, 6, 7, 8]
lis.sort()
print(halfFid(lis,7))

