# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:06:44 2019

@author: ls
"""
"""
题目24：二叉树中和为某一值的路径

题目描述：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

题目分析：
递归先序遍历树， 把结点加入路径。使用列表结构存树结构
若该结点是叶子结点则比较当前路径和是否等于期待和，叶子节点说明该路径应该截止了
弹出结点，每一轮递归返回到父结点时，当前路径也应该回退一个结点。

"""
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
 
        ret = []
        path = []
        self.Find(root, expectNumber, ret, path)
        # print ret
        # a = [];self.f(a);print a
        return ret
     
    def Find(self, root, target, ret, path):
        if not root:
            return
 
        path.append(root.val)
        isLeaf = (root.left is None and root.right is None)
        if isLeaf and target == root.val:
            ret.append(path[:])  # 这里这一步要千万注意啊，
            # 假如是:ret.append(path), 结果是错的。因为Python可变对象都是引用传递啊。
 
        #print "target:", target, "isLeaf:", isLeaf,
        #print "val:", root.val, "path:", path, "ret:", ret
        #print
 
        if root.left:
            self.Find(root.left, target - root.val, ret, path)
        if root.right:
            self.Find(root.right, target - root.val, ret, path)
 
        path.pop()
