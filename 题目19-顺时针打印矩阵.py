# -*- coding: utf-8 -*-
"""
题目19：顺时针打印矩阵

题目描述：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

题目分析：
可以模拟魔方逆时针的方法，一直做取出第一行的操作
例如
1  2  3  4
5  6  7  8
9 10 11  12
13 14 15 16

输出（1 2 3 4）并删除第一行后，再进行一次逆时针旋转，就变成
8 12 16
7 11 15
6 10 14
5  9 13

继续重复上述操作即可
"""
class Solution:
    #matrix类型为二维列表，需要返回列表
    def printMatrix(self,matrix):
        result = []#存放要输出的数据
        while(matrix):#最外层的循环控制是矩阵是否为空
            result += matrix.pop(0)#x=matrix.pop(0)删除matrix的第一行并返回第一行[1,2,3,4]
            if not matrix:
                break#如果矩阵matrix取出第一行后为空，则直接跳出循环
            matrix = self.turn(matrix)#调用翻转函数
        return result
    def turn(self,matrix):
        newmat = []#存放反转后的矩阵结果
        row = len(matrix)#行
        col = len(matrix[0])#列
        for i in range(col):
            newmat1 = []#存放列数据
            for j in range(row):
                newmat1.append(matrix[j][i])
            newmat.append(newmat1)#此时，只是把矩阵的行和列颠倒，
            """
输入矩阵：  1  2  3  4          输出矩阵： 1 5 9 13
          5  6  7  8                   2 6 10 14
          9 10 11  12                  3 7 11 15
          13 14 15 16                  4 8 12 16
            """
        newmat.reverse()#reverse()是列表中的内置函数，矩阵上下反转，
        return newmat
"""
输入矩阵： 1 5 9  13             输出矩阵：4 8 12 16
         2 6 10 14                     3 7 11 15
         3 7 11 15                     2 6 10 14
         4 8 12 16                     1 5 9  13
"""        
