# -*- coding: utf-8 -*-



"""

题目18：二叉树的镜像
题目描述：操作给定的二叉树，将其变换为原二叉树的镜像。
二叉树的镜像定义：源二叉树 

    	    8

    	   /  \

    	  6   10

    	 / \  / \

    	5  7 9 11

    	镜像二叉树

    	    8

    	   /  \

    	  10   6

    	 / \  / \

    	11 9 7  5
"""  
###############递归######################

class Solution:

    #返回镜像树的根节点

    def Mirror(self,root):

        if not root:

            return root

        root.left,root.right = root.right,root.left

        self.Mirror(root.left)

        self.Mirror(root.right)

        return root
