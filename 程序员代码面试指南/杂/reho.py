# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:13:30 2019

@author: comnet
"""
class Solution:
    def main(self,n,k):
        ress = set()
        all = [ int(i) for i in range(1,n+1)]
        for i in all:
            all1 = all[:]
            all1.remove(i)
            self.one(all1,k-1,[i],ress)
        for a in ress:
            print(list(a)) 
    def one(self,all,k,res,ress):
        if k==0:
            res.sort()
            ress.add(tuple(res))
        else:
            for i in all:
                res1= res[:]
                all1 = all[:]
                all1.remove(i)
                self.one(all1,k-1,res1+[i],ress)
tset = Solution()
tset.main(50,49)