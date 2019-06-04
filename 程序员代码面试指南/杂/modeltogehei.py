# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:31:50 2019

@author: comnet
"""

filename = '字典部分.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径
zidian = {}
with open(filename, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline() # 整行读取数据
        if not lines:
            break
        line = lines.split() # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
        zidian[line[0]] = line[1]
filename = 'bian.txt'
all = []
with open(filename, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline() # 整行读取数据
        if not lines:
            break
        line = lines.split() # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
        line[0] = zidian[line[0]]
        line[1] = zidian[line[1]]
        all.append(line[0]+' '+line[1]+' '+line[2])