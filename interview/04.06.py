'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 14:47:20
LastEditors: lmio 2091319361@qq.com
Description: 面试题 04.06. 后继者
'''

from utils.node import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        pre = float('-inf')
        res = None
        def f(node: TreeNode):
            nonlocal pre, res, p
            if not node:
                return
            f(node.left)
            if p == pre:
                res = node
            pre = node
            if not res:
                f(node.right)
        f(root)
        return res