# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:13:07 2019

@author: comnet
"""
#import time
#start = time.process_time()


import cProfile
def foo():
    for i in range(1,100000):
        n = str(i**2)
        if n == n[::-1]:
            print(i,i**2)
            


cProfile.run('foo()')
