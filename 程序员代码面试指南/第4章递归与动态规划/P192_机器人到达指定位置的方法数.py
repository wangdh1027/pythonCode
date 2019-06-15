# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:26:01 2019
机器人到达指定位置的方法数
@author: comnet
"""

def way(n,m,k,p):
    if n<2 or k<1 or m<1 or m>n or p<1 or p>n:
        return 0
    dp = [0]*(n+1)
    dp[p] = 1
    for i in range(1,k+1):
        leftup = dp[1]
        for j in range(1,n+1):
            tmp = dp[j]
            if j==1:
                dp[j] = dp[j+1]
            elif j==n:
                dp[j] = leftup
            else:
                dp[j] = leftup + dp[j+1]
            leftup = tmp
        print(dp)
    return dp[m]
print(way(7,4,9,5))