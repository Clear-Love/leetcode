'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 14:32:20
LastEditors: lmio 2091319361@qq.com
Description: 面试题 04.05. 合法二叉搜索树
'''

from utils.node import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float('-inf')
        def f(node: TreeNode) -> bool:
            nonlocal pre
            if not node:
                return True
            l = f(node.left)
            if node.val <= pre:
                return False
            pre = node.val
            r = f(node.right)
            return l and r
        return f(root)