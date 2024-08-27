'''
Author: lmio 2091319361@qq.com
Date: 2024-03-19 21:50:37
LastEditors: lmio 2091319361@qq.com
Description: 235. 二叉搜索树的最近公共祖先
'''

from utils.node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ancestor(node: TreeNode):
            if not node:
                return
            if node == p or node == q:
                return node
            left = ancestor(node.left)
            right = ancestor(node.right)
            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right
            return None
        return ancestor(root)