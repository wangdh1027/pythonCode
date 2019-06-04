# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:09:06 2019
讲一个字符串全部割成回文串粗腰的最少次数
@author: comnet
"""

def minCut(s):
    """
    :type s: str
    :rtype: int
    """
    if not s or s == s[::-1]: return 0
    n = len(s)
    for i in range(1, n):
        if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
            return 1
    dp = list(range(-1, n))
    print(dp)
    for i in range(n):
        for k in range(0, min(n - i, i + 1)):
            if s[i + k] != s[i - k]:
                break
            dp[i + k + 1] = min(dp[i + k + 1], dp[i - k] + 1)
        for k in range(1, min(n - i, i + 2)):    
            if s[i + k] != s[i - k + 1]:
                break
            dp[i + k + 1] = min(dp[i + k + 1], dp[i - k + 1] + 1)
    print(dp)
    return dp[n]
print(minCut('gwdwarer13'))