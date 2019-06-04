# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:38:00 2019
子数组异或和为0最多的划分
@author: comnet
"""
def maxyihuo(arr):
    dp = [0]*len(arr)
    dp[0] = 1 if arr[0] == 0 else 0
    Map = {}
    eor = 0
    Map[arr[0]] = 0
    Map[0] = -1
    for index in range(1,len(arr)):
        eor ^= arr[index]
        if eor in Map:
            dp[index] = dp[Map[eor]]+1 if Map[eor]!=-1 else 1 
        dp[index] = max(dp[index],dp[index-1])
        Map[eor] = index
    return dp[-1]
print(maxyihuo([3,2,1,9,0,7,0,2,1,3]))
    