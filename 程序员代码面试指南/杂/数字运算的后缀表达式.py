# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:27:50 2019
A+B*(C-D)/E的后缀表达式
ABCD-*E/+

PDF  P153
@author: comnet
"""
mydict = {'A': np.asarray([1, 0, 0, 0]), 'G': np.asarray([0, 1, 0, 0]),
        'C': np.asarray([0, 0, 1, 0]), 'T': np.asarray([0, 0, 0, 1]),
        'N': np.asarray([0, 0, 0, 0]), 'H': np.asarray([0, 0, 0, 0]),
        'a': np.asarray([1, 0, 0, 0]), 'g': np.asarray([0, 1, 0, 0]),
        'c': np.asarray([0, 0, 1, 0]), 't': np.asarray([0, 0, 0, 1]),
        'n': np.asarray([0, 0, 0, 0]), '-': np.asarray([0, 0, 0, 0])}