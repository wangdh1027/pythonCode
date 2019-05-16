# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:06:20 2019
打猎游戏
@author: comnet
"""
def path(i,p,d,d_all,p_all):
    if d_all>=p_all[i] or i==len(p) :
        return 0
    else:
        if d_all<d[i]:
            return(path(i+1,p,d,d_all+d[i],p_all)+p[i])
        else:
            return min(path(i+1,p,d,d_all+d[i],p_all)+p[i],path(i+1,p,d,d_all,p_all))
def main(d,p):   
    n = p[:]
    n.reverse()
    p_amx = [n[0]]
    for i in range(1,len(n)):
        p_amx.append(max(p_amx[-1],n[i]))
    return path(0,p,d,0,p_amx)
    
N = 24
#d = [4,5,1,2,4,66,7,9,4,66,7,9,4,66,7,9,4,66,7,92,4,66,7,9]
#p = [1,8,6,8,6,83,6,8,6,38,6,8,6,28,6,8,6,83,6,83,6,83,6,8]
d = [4,5,1,3]
p = [1,8,6,4]
print(main(d,p))