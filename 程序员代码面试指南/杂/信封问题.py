# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:41:10 2019
信封问题
每个信封都有长和宽 a的长和宽都比b小时，a可以装到b里
求最多可以套几层

将长度升序排列，长度相等时，按照宽度降序排列
排列完成后，将所有的宽度取出成为新的数组，求这个数组的最大升序列 即为可以嵌套的层数

@author: comnet
"""


"""
输入方法
n = int(input())
A = list(map(int, input().split(' ')))
"""
a= [1,2]
n = 3
for i in a:
    if n==9:
        break
    print(i)
    a.append(n)
    n+=1