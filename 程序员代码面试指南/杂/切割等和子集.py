# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:44:44 2019
分割等和子集
@author: comnet
"""
List = [2,2,2,6]
def canPartition(nums):
    su = sum(nums)
    if su%2 == 1:
        return False
    lis1 = [0]*su
    lis2 = [0]*su
    for val in nums:
        lis1[val-1] = 1
        for index2,val2 in enumerate(lis2):
            if val2 == 1:
                lis1[index2] = 1
                lis1[index2+val] = 1
        if lis1[int(su/2)-1]:
            return True
        lis1,lis2 = lis2,lis1
    return False
print(canPartition(List))
