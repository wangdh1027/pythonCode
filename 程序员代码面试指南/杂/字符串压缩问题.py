# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:15:00 2019

@author: comnet
"""

inputs = '3{d}2{aaabc3{dfs}}aarwr'
#inputs = 'ww'

def main(inputs,i):
    res = ''
    while i<len(inputs):
        if inputs[i]>='a' and inputs[i]<='z':
            res += inputs[i]
            i+=1
        elif inputs[i] =='}':
            return res,i+1
        elif inputs[i]>='0' and inputs[i]<='9':
            res1,j =  main(inputs,i+2)
            res+=int(inputs[i])*res1
            if j<len(inputs):
                i = j            
            else:
                return res,len(inputs)
    return res,len(inputs)
r,l = main(inputs,0)