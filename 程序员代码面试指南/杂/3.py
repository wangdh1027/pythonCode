# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:34:20 2019

@author: comnet
"""
in_put = [1,2,0,7,4,4,3,5]
res = 0
for i in range(len(in_put)):
    while(in_put[i]!=i):
        if in_put[i]==in_put[in_put[i]]:
            print(in_put[i])
            res = 1
            break
        in_put[in_put[i]],in_put[i]=in_put[i],in_put[in_put[i]]
    if res:
        break