# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:57:02 2019
 0 1 & | ^ 五种字符组成的字符串为Ture或者False的可能性
@author: comnet
"""
import numpy as np
def getnum(arr):
    size = len(arr)
    turearr = np.zeros([size,size])
    falsearr = np.zeros([size,size])
    for i in range(0,size,2):
        turearr[i,i] = 1 if arr[i]== '1' else 0
        falsearr[i,i] = 1 if arr[i] == '0' else 0
    for row in range(2,size,2):
        for col in range(row-2,-1,-2):
            turenum = 0
            falsenum = 0
            for i in range(row-1,0,-2):
                a = turearr[row,i+1]
                b = falsearr[row,i+1]
                c = turearr[i-1,col]
                d = falsearr[i-1,col]
                if arr[i] =='&':
                    turenum += a*c
                    falsenum += b*c+b*d+a*d
                elif arr[i] =='|':
                    turenum += a*c+a*d +b*c
                    falsenum += b*d         
                else:
                    turenum += a*d +b*c
                    falsenum += a*c+b*d   
                turearr[row,col] = turenum
                falsearr[row,col] = falsenum
    return int(turearr[size-1,0]),int(falsearr[size-1,0])
arr = '1^0&0|1&1^0&0^1|0|1&1'
#     Ture   False
res = getnum(arr)
print('Ture:',res[0],'False:',res[1])