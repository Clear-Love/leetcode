'''
Author: lmio 2091319361@qq.com
Date: 2023-07-09 21:02:34
LastEditors: lmio 2091319361@qq.com
Description: 222. 完全二叉树的节点个数
'''

from typing import Optional

from utils.node import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)