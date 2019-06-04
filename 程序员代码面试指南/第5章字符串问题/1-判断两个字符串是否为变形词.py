# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:52:28 2019

@author: comnet
"""
str1 = 'asdasdaseeqwgf'
str2 = '2fsdfsdff23faf'
def isDeformation(str1,str2):
    if len(str1)!=len(str2):
        return 0
    else:
        maps = {}
        for tmp in str1:
            if tmp in maps:
                maps[tmp] += 1
            else:
                maps[tmp] = 1
        for tmp in str2:
            if tmp in maps:
                maps[tmp] -=1
            else:
                return 0
        for tmp in maps:
            if maps[tmp] !=0:
                return 0
        return 1

if isDeformation(str1,str2):
    print('yes')
else:
    print('no')