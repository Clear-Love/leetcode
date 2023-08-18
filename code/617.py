'''
Author: lmio 2091319361@qq.com
Date: 2023-08-14 16:53:27
LastEditors: lmio 2091319361@qq.com
Description: 617. 合并二叉树
'''

from typing import Optional
from utils.node import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        elif root1:
            return root1
        else:
            return root2