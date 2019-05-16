# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:05:35 2019

@author: comnet
"""



inputs = []
one = input()
while one:
    inputs.append(list(map(int, one.split(' '))))
    one = input()
list2 = []
num1 = 0
for i in range(len(inputs)):
    for j in range(len(inputs[0])):
        if inputs[i][j] == 2:
            list2.append([i,j])
        elif inputs[i][j] == 1:
            num1+=1
res = 0
list1 = list2[:]
while list1:
    list2= list1[:]
    list1 = []
    tmp = 0
    for two in list2:
        i = two[0]
        j = two[1]
        if i-1>=0:
            if inputs[i-1][j] == 1:
                tmp =1
                num1-=1
                inputs[i-1][j] =2
                list1.append([i-1,j])
        if i+1<len(inputs):    
            if inputs[i+1][j] == 1:
                tmp =1
                num1-=1
                inputs[i+1][j] =2
                list1.append([i+1,j])
        if j-1>=0:
            if inputs[i][j-1] == 1:
                tmp =1
                num1-=1
                inputs[i][j-1] =2
                list1.append([i,j-1])
        if j+1<len(inputs[0]):   
            if inputs[i][j+1] == 1:
                tmp =1
                num1-=1
                inputs[i][j+1] =2
                list1.append([i,j+1])
    if tmp:
        res+=1
if num1==0:          
    print(res)
else:
    print(-1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        