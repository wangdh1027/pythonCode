# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:29:05 2019

@author: comnet
"""

'''
一个数组可正  可负 可0   求一个和 小于等于sum的最长子数组
'''
'''
minsum    以此位置为开始 的子数组能够得到的最小累加和 
minsum-in 这个数组的右边界到哪
arr         7       5     4    -3    -1  
minsum      7       5     0    -4    -1
minsum_in   N-5    N-1    N-1  N-1   N-1

从后往前算 dp


从第0开始算，若 minsum[0]<sum,则看第minsum_in[0] 位， 比较 minsum[0]+minsum[minsum_in[0]+1] 与 sum
一直往后比 ，直到找出从第0位开始  最长的比sum小的子数组

然后把arr[0]去掉，看是否符合条件
'''
def maxLong(arr,su):
    size = len(arr)
    if size == 0:
        return 0
    sums = [0]*size
    ends = [0]*size
    sums[-1] = arr[-1]
    ends[-1] = size-1
    for i in range(size-2,-1,-1):
        if sums[i+1]<=0:
            sums[i] = arr[i]+sums[i+1]
            ends[i] = ends[i+1]
        else:
            sums[i] = arr[i]
            ends[i] = i
    end = 0
    s = 0
    res = 0
    for i in range(size):
        while(end<size and s+sums[end]<=su):
            s+=sums[end]
            end = ends[end]+1
        s -= arr[i] if end>i else 0
        res = max(res,end-i)
        end = max(end,i+1)
    return res 
        


print(maxLong([7,-4,4,-3,9],3))
















