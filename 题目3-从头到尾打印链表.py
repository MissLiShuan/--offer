"""
题目3：从尾到头打印链表

输入一个链表，按链表值从尾到头的顺序返回一个ArrayList

"""


'''
方法一：使用extend，在尾部插入，其实最关键在于[::-1],只不过输入数据多样化，有可能还是集合，所以转成列表
这个方法效率应该还可以，先存入vector，再反转vector
26ms
5512k
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution1:
    #返回从尾部到头部的列表值序列，[1,2,3]
    def printListFromTailToHead(self,listNode):
        if not listNode:
            return []
        result = []
        while listNode.next is not None:
            result.extend([listNode.val])
            listNode = listNode.next
        result.extend([listNode.val])
        return result[::-1]#将列表反转
'''
append和extend的区别：
append是整体添加
l1 = [1, 2, 3, 4, 5, ]
l1.append([6, 7, 8, 9, ])
# l1.append(*[6, 7, 8, 9, ]) #会报错
print(l1)
l1.extend([6, 7, 8, 9])
print(l1)
extend是逐个添加
l1 = [1, 2, 3, 4, 5, ]
l1.extend([6, 7, 8, 9])
print(l1)
l1.extend('abc')
print(l1)
l1.extend('a') # 也是可迭代对象
print(l1)
# l1.extend(1) # 报错，不可迭代
print(l1)

# 输出

[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c']
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'a']
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'a']


'''
方法二： 使用insert直接在头部插入
26ms
6336k
'''

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        result = []
        head = listNode
        while head:
            result.insert(0, head.val)
            head = head.next
        return result
'''
