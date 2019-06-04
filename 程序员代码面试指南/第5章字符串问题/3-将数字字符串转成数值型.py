# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:18:41 2019

@author: comnet
"""
def isValid(str1):
    if str1[0] != '-' and (str1[0] <'0' or str1[0]>'9'):
        return False
    if str1[0] == '-' and (len(str1) ==1  or str1[0] == '0'):
        return False
    if str1[0] =='0' and len(str1)>1:
        return False
    for i in range(1,len(str1)):
        if str1[i]<'0' or str1[i]>'9':
            return False
    return True
def convert(str1):
    if str1 == None or len(str1)==0 or not isValid(str1):
        return 0
    else:
        return int(str1)
print(convert('-1231'))