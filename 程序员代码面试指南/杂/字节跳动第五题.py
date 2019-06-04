# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:47:37 2019

@author: comnet
"""
import sys 
inp = []
one = input()
while one:
    inp.append(list(map(int, one.split(' '))))
    one = input()
    
for i in range(2,len(inp),2):
    inputs = inp[i][:]
    size = inp[i-1]
    if size == 2:
        print(max(inputs))
    else:
        min1 = min(inputs)
        inputs.remove(min1)
        min2 = min(inputs)
        inputs.remove(min2)
        tmp = max(min1,min2)
        res  = sum(inputs) + max((min1,min2)*size-3)
        print(res)