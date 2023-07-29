'''
Author: lmio 2091319361@qq.com
Date: 2023-07-29 16:22:42
LastEditors: lmio 2091319361@qq.com
Description: 1372. 二叉树中的最长交错路径
'''
from typing import Optional

from utils.node import TreeNode


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node: TreeNode, isLeft: bool, length: int):
            nonlocal res
            if not node:
                return
            res = max(res, length)
            if isLeft:
                dfs(node.left, False, length+1)
                dfs(node.right,True, 1)
            else:
                dfs(node.left, False, 1)
                dfs(node.right,True, length+1)
        dfs(root, True, 0)
        return res