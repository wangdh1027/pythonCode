# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:59:10 2019
@author: comnet
"""
#时间复杂度：O(n**2) 
def getdp1(matrix):
    matrix.sort(key=lambda tmp:tmp[0]*1000000-tmp[1]) #按照长度升序，宽度降序排列
    #然后看宽度的最长递增子序列就行
    dp = [0]*len(matrix)
    for i in range(len(matrix)):
        dp[i] = 1
        for j in range(i):
            if matrix[i][1]>matrix[j][1]:
                dp[i] = max(dp[i],dp[j]+1)
    return dp

#时间复杂度：O(nlog(n)) 
def getdp2(matrix):
    matrix.sort(key=lambda tmp:tmp[0]*1000000-tmp[1]) #按照长度升序，宽度降序排列
    #然后看宽度的最长递增子序列就行
    dp = [0]*len(matrix)
    ends = [0]*len(matrix)
    dp[0] = 1
    right = 0
    l = 0
    r = 0
    m = 0
    for i in range(1,len(matrix)):
        l = 0
        r = right
        while l <= r:
            m = int((l+r)/2)
            if matrix[i][1]>ends[m]:
                l = m+1
            else:
                r = m-1
        right = max(right,l)
        ends[l] = matrix[i][1]
        dp[i] = l
    return dp


matrix = [[3,4],[2,3],[4,5],[1,3],[2,2],[3,6],[1,2],[3,2],[2,4]]
print(getdp1(matrix),getdp2(matrix))