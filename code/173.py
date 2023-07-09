'''
Author: lmio 2091319361@qq.com
Date: 2023-07-09 20:48:20
LastEditors: lmio 2091319361@qq.com
Description: 173. 二叉搜索树迭代器
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)
    
    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def hasNext(self):
        return len(self.stack) > 0
    
    def next(self):
        node = self.stack.pop()
        if node.right:
            self._leftmost_inorder(node.right)
        return node.val
