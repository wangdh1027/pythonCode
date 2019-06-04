# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:56:52 2019

@author: comnet
"""

    
n = 10
res = [1]*(n+1)
res[2] = 2
res[3] = 3
for i in range(4,n+1):
    maxi = 0
    for j in range(1,int(i/2)+1):
       maxi = max(maxi,res[j]*res[i-j])
    res [i] = max(i,maxi)
print(res)