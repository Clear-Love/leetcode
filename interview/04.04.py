'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 13:44:34
LastEditors: lmio 2091319361@qq.com
Description: 面试题 04.04. 检查平衡性
'''

from utils.node import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def f(node: TreeNode, h: int) -> (bool, int):
            if not node:
                return True, h
            l, hl = f(node.left, 0)
            r, hr = f(node.right, 0)
            return l and r and abs(hl-hr) <= 1, max(hl, hr)+1
        res, _ = f(root, 0)
        return res