'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 15:47:00
LastEditors: lmio 2091319361@qq.com
Description: 面试题 04.08. 首个共同祖先
'''

from utils.node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def f(node: TreeNode) -> TreeNode:
            if not node:
                return None
            if node == p or node == q:
                return node
            left = f(node.left)
            right = f(node.right)
            if left and right:
                return node
            elif left:
                return left
            else:
                return right
        return f(root)