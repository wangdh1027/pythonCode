# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 20:15:55 2019

@author: comnet
"""

#n = int(input())
#m = int(input())
#k = int(input())
n = 2
m = 1
k = 3
mlist = list(range(1,m))
nlist = list(range(1,n))

def num(n,m,k,mlist,nlist):
    if k == 0 or (n==0 and m==0):
        return 1
    res = 0
    if len(nlist)>=0:
        for i in nlist:
            if i<=n:
                nlist.remove(i)
                res+=num(n-i,m,k-1,mlist,nlist)
            if len(nlist)==0:
                break
    if len(mlist)>=0:
        for i in mlist:
            if i<=m:
                mlist.remove(i)
                res+=num(n,m-i,k-1,mlist,nlist)  
            if len(mlist)==0:
                break
    res += num(n,m,k-1,mlist,nlist) 
    return res
print(num(n,m,k-2,mlist,nlist))