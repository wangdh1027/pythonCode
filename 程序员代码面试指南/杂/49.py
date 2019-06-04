# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:59:03 2019
丑数
@author: comnet
"""

def choushu(n):
    lis = [1]
    t2 = t3 = t5 = 0
    T2 = T3 = T5 = 0
    a = 1
    while(1):
        for i in range(t2,len(lis)):
            if 2*lis[i]>lis[-1]:
                T2 = 2*lis[i]
                t2 = i
                break
        for i in range(t3,len(lis)):
            if 3*lis[i]>lis[-1]:
                T3 = 3*lis[i]
                t3 = i
                break
        for i in range(t5,len(lis)):
            if 5*lis[i]>lis[-1]:
                T5 = 5*lis[i]
                t5 = i
                break
        maxone = min(T2,T3,T5)
        a+=1
        lis.append(maxone)
        if a==n:
            break
    return maxone
print(choushu(1500))
            
