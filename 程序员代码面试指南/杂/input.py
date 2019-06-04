# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:58:43 2019

@author: comnet
"""
#n = int(input())
#plist = []
#for i in range(n):
#    plist.append(float(input()))
    
    
    
plist = [0.6,0.4,0.5]
p1 = 0
p2 = 0
p = 1
num = 1
for i in range(5):
    for one in plist:
        if num:
            p1 += p*one 
            p *= (1-one)
            num=0
        else:
            p2 += p*one
            p *= (1-one)
            num=1
print(p1/(p1+p2))
print ('%.4f'%(p1/(p1+p2+p)))