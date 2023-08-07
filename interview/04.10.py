'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 16:27:53
LastEditors: lmio 2091319361@qq.com
Description: 面试题 04.10. 检查子树
'''

from utils.node import TreeNode


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t2:
            return True
        if not t1:
            return False
        return self.isTreeEql(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)
    def isTreeEql(self, t1: TreeNode, t2: TreeNode) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and self.isTreeEql(t1.left, t2.left) and self.isTreeEql(t1.right, t2.right)