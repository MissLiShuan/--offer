
题目描述：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。

题目分析：
二叉搜索树即是二叉排序树，
1. 后序遍历序列的最后一个元素为二叉树的根节点；
2. 二叉搜索树左子树上所有的结点均小于根结点、右子树所有的结点均大于根结点。

算法步骤如下：
1. 找到根结点；
2. 遍历序列，找到第一个大于等于根结点的元素i，则i左侧为左子树、i右侧为右子树；
3. 我们已经知道i左侧所有元素均小于根结点，那么再依次遍历右侧，看是否所有元素均大于根结点；
若出现小于根结点的元素，则直接返回false；若右侧全都大于根结点，则：
4. 分别递归判断左/右子序列是否为后序序列；
"""
class Solution:
    def VerifySquenceOfBST(self,sequence):
        #1.首先判定序列是否为空
        if len(sequence)==0:
            return False
        
        index = 0
        #2.遍历整个序列，找到第一个大于根结点的元素i的索引index,
        for i in range(len(sequence)):
            if sequence[i]>sequence[-1]:
                index = i
                break
        #遍历index后面的节点，如果后面的节点小于根节点，则说明该数组不是某二叉搜索树的后序遍历的结果
        for j in range(i,len(sequence)):
            if sequence[j]<sequence[-1]:
                return False
        
        left = True
        right = True
        if len(sequence[:index])>0:
            left = self.VerifySquenceOfBST(sequence[:index])
            #index左侧为左子树，
        if len(sequence[index:-1])>0:
            right = self.VerifySquenceOfBST(sequence[index:-1])
            #index右侧为右子树
        return left and right
