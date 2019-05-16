# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:08:33 2019
最长有效括号字符串
@author: comnet
"""

def maclen(arr):
    dp = [0]*len(arr)
    pre = 0
    res = 0
    for i,val in enumerate(arr):
        if val == ')':
            pre = i-dp[i-1]-1
            if pre >= 0 and arr[pre] =='(':
                dp[i] = dp[i-1] + 2 
                if pre-1 > 0:
                    dp[i] += dp[pre-1]
        res = max(res,dp[i])
    return res,dp
arr = '()()()()()()()()(((()))))'
print(maclen(arr))