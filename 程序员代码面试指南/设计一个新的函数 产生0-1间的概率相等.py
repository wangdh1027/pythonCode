# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:44:21 2019
ran() P的概率产生1 (1-p)的概率产生0
设计一个新的函数 产生0-1间的概率相等 
@author: comnet
"""

import random
num = 0
def ran():
    a = random.random()
    return 0 if a<0.25 else 1
def newran():
    global num
    a1 = ran()
    a2 = ran()
    num+=1
    if a1==0 and a2 ==1:
        return 0
    elif a1==1 and a2 ==0:
        return 1
    else:
        return newran()
a0 = 0
a1 = 0
res = 0
for i in range(1000000):
    if newran()==0:
        a0+=1
    else:
        a1+=1
    res = max(res,num)
    num = 0
print(a0,a1,res)