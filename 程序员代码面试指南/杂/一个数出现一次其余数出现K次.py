# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:10:23 2019
一个数出现一次 其余数出现K次


将每个数都转化为K进制存在e中，并且将e中每个位置都模K，最后再将e转化为十进制 即为答案

@author: comnet
"""
def onceNum(arr,k):
    e = [0]*32
    for n in arr:
        index = 0
        while n!=0:
            e[index] = (e[index]+n%k)%k
            index += 1
            n = int(n/k)
    res = 0
    for index,i in enumerate(e):
        res += i*(3**index)
    return res
res = onceNum([ -1, -1, -1, -1, -1, 2, 2, 2, 4, 2, 2],5)
print(res)  