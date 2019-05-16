# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:04:41 2019
单链表的约瑟夫问题
共有n个节点的环形链表  数到第m个则将第m个去掉
最后剩的是谁
@author: comnet
"""


def lastNumber(n,m):
    if n==1:
        return 1
    else:
        return (lastNumber(n-1,m)+m-1)%n+1
print(lastNumber(10,3)) 


