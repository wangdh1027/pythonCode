# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:15:19 2019

@author: comnet
"""
#class Solution:
#    def reOrderArray(self, array):
#        # write code here
#        if array is not None:
#            for i in range(len(array)):
#                if array[i]%2==1 and i>0:
#                    for j in range(i,1,-1):
#                        if array[j-1]%2==0:
#                            array[j],array[j-1] = array[j-1],array[j]
#                        else:
#                            break
#
##                        print(array[j],array[j-1])
#        print (array)
#a = Solution()
#a.reOrderArray([1,2,4,5,6,7,8,])
from  scipy.stats import  ttest_ind
import pandas as pd
x = [21,22,23,24,25,25]
y = [13,14,15]
res = ttest_ind(x, y)
print(res)
##
#str1 = 'horse'
#str2 = 'ros'
#arr = [[0 for i in range(len(str1)+1)] for i in range(len(str2)+1)]
#for i in range(len(arr[0])):
#    arr[0][i]=i
#for i in range(0,len(arr)):
#    arr[i][0]=i
#for i in range(1,len(arr[0])):
#    for j in range (1,len(arr)):
#        one = arr[j-1][i-1] if str2[j-1] == str1[i-1] else arr[j-1][i-1]+1
#        arr[j][i] = min(arr[j-1][i]+1,arr[j][i-1]+1,one)
#print(arr[-1][-1])
#class Solution:
#    def minDistance(self, word1: str, word2: str) -> int:
#        str1 = word1
#        str2 = word2
#        arr = [[0 for i in range(len(str1)+1)] for i in range(len(str2)+1)]
#        for i in range(len(arr[0])):
#            arr[0][i]=i
#        for i in range(0,len(arr)):
#            arr[i][0]=i
#        for i in range(1,len(arr[0])):
#            for j in range (1,len(arr)):
#                one = arr[j-1][i-1] if str2[j-1] == str1[i-1] else arr[j-1][i-1]+1
#                arr[j][i] = min(arr[j-1][i]+1,arr[j][i-1]+1,one)
#                print(arr)
#        print(arr[-1][-1])
#        return arr[-1][-1]
#    
#    
#test = Solution
#res = test.minDistance(test,'horse','ros')