# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:29:18 2019
连续子数组的最大和
@author: comnet
"""
List = [1,34,-7,35,-94,26]     
def maxsonnum(List):
    if len(List) == 0:
        return 0
    i_max = res=List[0]
    for i in range(1,len(List)):
        i_max = List[i] if i_max<0 else i_max+List[i]
        res = max(res,i_max)
    return res
print(maxsonnum(List))