# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:16:25 2019
先序列中序列直接变后序
@author: comnet
"""
def post(perarr,inarr):
    if len(perarr) == 0:
        return None
    if len(perarr) == 1:
        return perarr
    res = [perarr[0]]
    inleft = inarr[:inarr.index(res[0])]
    inright = inarr[inarr.index(res[0])+1:]
    perleft = perarr[1:len(inleft)+1]
    perright = perarr[len(inleft)+1:] 
    tmp = post(perright,inright)
    if tmp!=None:
        res+=tmp
    tmp = post(perleft,inleft)
    if tmp!=None:
        res+=tmp
    return res
perarr = [1,2,4,5,3,6,7]
inarr = [4,2,5,1,6,3,7]
print(post(perarr,inarr)[::-1])
