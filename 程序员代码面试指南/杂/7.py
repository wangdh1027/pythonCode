# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:38:09 2019

@author: comnet
"""
class TreeNode(object):
    def __init__(self,val,l=0,r=0):
        self.val = val
        self.left = l
        self.right = r
perorder = [1,2,4,7,3,5,6,8]
inorder = [4,7,2,1,5,3,8,6]
def tree(perorder,inorder,root):
    if perorder or inorder:
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                root_i = i
                break
        leftperorder = perorder[1:root_i+1]
        rightperorder = perorder[root_i+1:]
        if leftperorder:
            leftson = TreeNode(leftperorder[0])
            root.left = leftson
            leftinorder = inorder[:root_i]
            tree(leftperorder,leftinorder,leftson)
        if rightperorder:
            rightson= TreeNode(rightperorder[0])        
            root.right = rightson        
            rightinorder = inorder[root_i+1:]       
            tree(rightperorder,rightinorder,rightson)
if perorder:
    root = TreeNode(perorder[0])
    tree(perorder,inorder,root)