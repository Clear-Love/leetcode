'''
Author: lmio 2091319361@qq.com
Date: 2023-07-08 18:05:14
LastEditors: lmio 2091319361@qq.com
Description: 226. 翻转二叉树
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def invert(node: TreeNode):
        if not node:
            return None
        node.left, node.right = invert(node.right), invert(node.left)
        return node
    return invert(root)