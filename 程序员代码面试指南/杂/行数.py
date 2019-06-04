# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:46:45 2019

@author: comnet
"""
def numlines(path):
    files= os.listdir(path) #得到文件夹下的所有文件名称  
    res = 0 
    for file in files: #遍历文件夹  
         if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
              with open(path+"/"+file,encoding='utf-8') as f:
                  num = len(f.readlines())
              res += num
              print(path+"/"+file,num)
         else:
              res+=numlines(path+"/"+file)
    return res

import os  
path = "D:\python" #文件夹目录  
print('总行数 ',numlines(path))



