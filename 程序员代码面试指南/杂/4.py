# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:59:26 2019

@author: comnet
"""
n = 71
put = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
i = len(put)
res = False
if i==0:
    print(res)
i -=1
j = 0
while(i>=0 and j<len(put)):
    print(put[j][i])
    if put[j][i]==n:
        res = True
        break
    if put[j][i]>n:
        i-=1
    if put[i][j]<n:
        j+=1
print(res)