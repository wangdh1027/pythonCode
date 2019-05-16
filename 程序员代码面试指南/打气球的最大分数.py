# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:47:18 2019
打气球的最大分数
P204
@author: comnet
"""

def macCoins(arr):
    arr = [1]+arr+[1]
    dp = list([0]*len(arr) for i in range(len(arr)))
    for i in range(1,len(arr)-1):
        dp[i][i] = arr[i]*arr[i-1]*arr[i+1]
    for L in range(len(arr)-2,0,-1):
        for R in range(L+1,len(arr)-1):
            finalL = arr[L-1]*arr[L]*arr[R+1]+dp[L+1][R]
            finalR = arr[L-1]*arr[R]*arr[R+1]+dp[L][R-1]
            dp[L][R] = max(finalL,finalR)
            for i in range(L+1,R):
                dp[L][R] = max(dp[L][R],arr[L-1]*arr[i]*arr[R+1]+dp[i+1][R]+dp[L][i-1])
    import numpy as np
    dp = np.array(dp)
    print(dp[1:-1,1:-1])
    print(dp[1,-2])
arr = [4,2,3,5,1,6]
macCoins(arr)