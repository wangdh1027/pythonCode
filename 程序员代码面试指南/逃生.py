# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:39:30 2019
逃生
@author: comnet
"""
def bumson(listin,i):
    res = len(listin[i])
    for j in listin[i]:
        res+=bumson(listin,j)
    return res
n = int(input())
listin = [[] for i in range(n+1)]
for i in range(n-1):
    one = input().split()
    listin[int(one[1])].append(int(one[0]))
res = 1
for i in listin[1]:
    res = max(res,bumson(listin,i))
print(res)