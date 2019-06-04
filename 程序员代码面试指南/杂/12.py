# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:52:56 2019
回溯法
@author: comnet
"""

def pathfind(arr,arrboo,path,i,j):
    print (i,j,path)
    if path:
        if i-1>=0 and arrboo[i-1][j]==1 and arr[i-1][j]==path[0]:
            arrboo[i-1][j] = 0
            if pathfind(arr,arrboo,path[1:],i-1,j):
                return True
        if i+1<len(arr) and arrboo[i+1][j]==1  and arr[i+1][j]==path[0]:
            arrboo[i+1][j] = 0
            if pathfind(arr,arrboo,path[1:],i+1,j):
                return True
        if j-1>=0 and arrboo[i][j-1]==1  and arr[i][j-1]==path[0]:
            arrboo[i][j-1] = 0
            if pathfind(arr,arrboo,path[1:],i,j-1):
                return True
        if j+1<len(arr[0]) and arrboo[i][j+1]==1  and arr[i][j+1  ]==path[0]:
            arrboo[i][j+1] = 0
            if pathfind(arr,arrboo,path[1:],i,j+1):
                return True
        return False   
    else:
        return True
arr = [['a','b','t','g'],
       ['c','f','c','s'],
       ['j','d','e','h'],
       ]
arrboo = [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        ]
#arrboo =([1]*len(arr))*len(arr[0])
res = pathfind(arr,arrboo,list('fcj'),0,1)
def pathfind(arr,arrboo,path,i,j):
    print (i,j,path)
    if path:
        a1 = False
        if i-1>=0 and arrboo[i-1][j]==1 and arr[i-1][j]==path[0]:
            arrboo[i-1][j] = 0
            a1 = a1 or  pathfind(arr,arrboo,path[1:],i-1,j)
        if i+1<len(arr) and arrboo[i+1][j]==1  and arr[i+1][j]==path[0]:
            arrboo[i+1][j] = 0
            a1 = a1 or pathfind(arr,arrboo,path[1:],i+1,j)
        if j-1>=0 and arrboo[i][j-1]==1  and arr[i][j-1]==path[0]:
            arrboo[i][j-1] = 0
            a1 = a1 or pathfind(arr,arrboo,path[1:],i,j-1)
        if j+1<len(arr[0]) and arrboo[i][j+1]==1  and arr[i][j+1  ]==path[0]:
            arrboo[i][j+1] = 0
            a1 = a1 or pathfind(arr,arrboo,path[1:],i,j+1)
        return a1   
    else:
        return True
arr = [['a','b','t','g'],
       ['c','f','c','s'],
       ['j','d','e','h'],
       ]
arrboo = [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        ]
#arrboo =([1]*len(arr))*len(arr[0])
res = pathfind(arr,arrboo,list('fcj'),0,1)