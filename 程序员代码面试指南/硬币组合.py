# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:11:13 2019
硬币组合
@author: comnet
"""

import sys
a = [] 
for line in sys.stdin:
    a.append(line)
m = int(a[0].split(' ')[0])
n = int(a[0].split(' ')[1])
nlist = []
for i in range(n):
    nlist.append(int(a[i+1]))
nlist.sort()
res = [0]*len(nlist)
for i in range(1,m+1):
    tmp = i 
    for j in range(len(nlist)-1,-1,-1):
        res[j] = max(int(tmp/nlist[j]),res[j])
        tmp = tmp%nlist[j]
print(res)