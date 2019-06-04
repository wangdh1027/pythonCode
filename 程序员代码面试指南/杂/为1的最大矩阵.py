# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:44:58 2019

@author: comnet
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:37:21 2019
最大的1矩阵
exp:
1 0 1 1
1 1 1 0
1 1 1 0
res = 6

O(m*n)

@author: comnet
"""
def draStack(arr):
    stack = []
#    res = []
    maxres = 0
    for i in range(len(arr)):
        if not stack:
            stack.append([arr[i],i])
        elif arr[i]>stack[-1][0]:
            stack.append([arr[i],i])
        elif arr[i]==stack[-1][0]:
            continue  
        else:
            while stack[-1][0]>arr[i]:
                if len(stack)>=2:
#                    res.append([stack[-1][0],stack[-2][-1],i,(i-stack[-2][-1]-1)])
                    maxres = max(maxres,stack[-1][0]*(i-stack[-2][-1]-1))
                else:
#                    res.append([stack[-1][0],-1,i,stack[-1][0]*(i)])
                    maxres = max(maxres,stack[-1][0]*(i))
                stack.pop()
                if not stack:
                    break
            stack.append([arr[i],i])
    while stack:
        if len(stack)>=2:
#            for i in range(len(stack[-1])-1):
#            res.append([stack[-1][0],stack[-2][-1],len(arr),(len(arr)-stack[-2][-1]-1)])
            maxres = max(maxres,stack[-1][0]*(len(arr)-stack[-2][-1]-1))
            stack.pop()
        else:
#            for i in range(len(stack[-1])-1):
#            res.append([stack[-1][0],-1,len(arr),stack[-1][0]*(len(arr))])
            maxres = max(maxres,stack[-1][0]*(len(arr)))
            stack.pop()
#    print(arr,res)
    return maxres
         
#print(draStack([1,0,3,2,3]))        
def max1Matrix(arr):
    N = len(arr[0])
    tmp = [0]*N
    res = 0
    for tmpone in arr:
        for i in range(N):
            tmp[i] = (tmp[i]+tmpone[i]) if tmpone[i] ==1 else 0
        res = max(res,draStack(tmp))
#        print(tmp,res)
    return(res)

arr = [[1,1,1,1,0,1],
       [1,0,1,1,1,1],
       [1,1,0,1,1,1],
       [1,1,0,1,1,1],
       ]
print(max1Matrix(arr))






















    