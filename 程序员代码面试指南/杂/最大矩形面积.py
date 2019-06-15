# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:38:29 2019

@author: comnet
"""

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        size = len(heights)
        i = 0
        maxsize = 0
        stack = []
        while i < size:#遍历数组中所有的高度，也就是所有的矩形
            if len(stack) == 0 or heights[stack[-1]] < heights[i]:#如果当前栈是空的或者说构成了一个递增的矩形序列
                stack.append(i)#把当前下标加入栈中
                i += 1#进入下一个矩形
            else:
                j = stack.pop()#如果栈不为空且不构成递增矩形序列关系
                maxsize = max(maxsize, heights[j] * (i if not stack else i - stack[-1] - 1) )#更新最大面积
                
        return maxsize
class Solution1:
    def maximalSquare(self, matrix):
        maxmian = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]=='1':
                    matrix[i][j]=min(int(matrix[i-1][j-1]),int(matrix[i-1][j]),int(matrix[i][j-1]))+1
                    maxmian = max(maxmian,matrix[i][j])
        return maxmian*maxmian
test = Solution1()
tmaxsize = test.maximalSquare([["1","1","1","1","1"],
                               ["1","1","1","1","1"],
                               ["1","1","1","1","1"],
                               ["1","0","0","1","0"]])
print(tmaxsize)