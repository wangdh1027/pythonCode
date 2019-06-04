# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:44:21 2019

@author: comnet
"""

def getNext(str2):
    if len(str2)  == 1:
        return [-1]
    Next = [0] *(len(str2))
    Next[0] = -1
    Next[1] = 0
    i = 2
    cn = 0
    while i<len(Next):
        if str2[i-1] ==str2[cn]:
            cn+=1
            Next[i] = cn
            i+=1
        elif cn>0:
            cn = Next[cn]
        else:
            Next[i] = 0
            i+=1
    return Next
def getIndexOf(str1,str2):
    size1 = len(str1)
    size2 = len(str2)    
    if size2<1 or size1<size2:
        return -1
    i1 = 0
    i2 = 0
    Next = getNext(str2)
    while i1<size1 and i2<size2:
        if str1[i1]==str2[i2]:
            i1+=1
            i2+=1
        elif Next[i2] == -1:
            i1+=1
        else:
            i2 = Next[i2]
    return i1-i2 if i2==size2 else -1
 
str1 = 'eqweqw'
str2 = ' '
print(getNext(str1))
print(getIndexOf(str1,str2))