# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:59:43 2019
位运算实现加法
@author: comnet
"""
 
def add(num1,num2):
    sm = 0
    per = 1
    while per!=0:
        sm = num1^num2
        per = (num1&num2)<<1
        num1 = sm
        num2 = per
    return sm
print(add(0,1))
    

