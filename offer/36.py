'''
Author: lmio
Date: 2023-04-05 17:03:44
LastEditTime: 2023-07-14 20:12:46
FilePath: /leetcode/offer/36.py
Description: 剑指 Offer 36. 二叉搜索树与双向链表 (这道题不支持go语言)
'''

from utils.node import TreeNode as Node


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.pre = None
        def dfs(node: 'Node'):
            if not node:
                return
            dfs(node.left)
            if self.pre:
                self.pre.right, node.left = node, self.pre
            else:
                self.head = node
            self.pre = node
            dfs(node.right)
        dfs(root)
        if not root:
            return
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
