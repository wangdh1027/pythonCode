# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:15:57 2019

@author: comnet
"""

#coding:utf8
import os;

def rename():
    path=r"D:\工作\reho全脑_血液循环t检验\验证数据\c_r_汇总"
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(path,files);#原来的文件路径                
        if os.path.isdir(Olddir):#如果是文件夹则跳过
                continue;
        filename=os.path.splitext(files)[0];#文件名
        fileli = filename.split('_')
        if len(fileli)==3:
            print(fileli[0]+'_'+fileli[1].zfill(5)+'_'+'resting.nii')
            Newdir=os.path.join(path,fileli[0]+'_'+fileli[1].zfill(5)+'_'+'resting.nii');#新的文件路径
            os.rename(Olddir,Newdir)#重命名
#        if len(fileli)==2:
#            number = fileli[1].split('.')[0]
#            print(fileli[0]+'_'+number.zfill(5)+'_'+'resting.nii')
#            Newdir=os.path.join(path,fileli[0]+'_'+number.zfill(5)+'_'+'resting.nii');#新的文件路径
#            os.rename(Olddir,Newdir)#重命名
rename()