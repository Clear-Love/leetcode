'''
Author: lmio 2091319361@qq.com
Date: 2023-08-22 18:37:01
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.12. BiNode
'''

from utils.node import TreeNode


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def convert(root: TreeNode):
            if not root:
                return root, root
            begin=end=root
            if root.left:
                begin, end = convert(root.left)
                end.right = root
                end = root
                root.left=None
            if root.right:
                root.right, end = convert(root.right)
            return begin, end
        return convert(root)[0]