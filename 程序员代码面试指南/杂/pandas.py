# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:17:10 2019

@author: comnet
"""
import re
string = ['黄焖鸡米饭(人民广场店)',' (奶茶) 一点点','麦当劳(虹桥路)']
print([re.sub(pattern='((.*))$',repl='',string=i)for i in string])
print([re.sub(pattern='((.*))',repl='',string=i)for i in string])
print([re.sub(pattern='[ ((].*[)) ]',repl='',string=i)for i in string])
print([re.sub(pattern='[ ((].*[)) ]$',repl='',string=i)for i in string])