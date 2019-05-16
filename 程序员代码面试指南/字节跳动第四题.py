# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:27:57 2019

@author: comnet
"""

import sys 
inputs = []
n = 0
for line in sys.stdin:
    n = int(line)
    break
for line in sys.stdin:
    inputs.append(list(map(int, line.split(' '))))
for i