# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:08:04 2019

@author: comnet
"""
def isRotation(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        return str1 in str2+str2
print(isRotation('123456','234561'))