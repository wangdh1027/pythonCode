# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:12:12 2019

@author: comnet
"""

import sys 
inp = []
one = input()
while one:
    inp.append(list(map(int, one.split(' '))))
    one = input()
N = inp[0][0]
lines = 1
for i in range(N):
    n = inp[lines][0]
    for j in range(lines+1,lines+n+1):
        
        
        
        
    lines += (n+1) 