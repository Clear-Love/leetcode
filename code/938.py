'''
Author: lmio 2091319361@qq.com
Date: 2024-03-19 21:59:14
LastEditors: lmio 2091319361@qq.com
Description: 938. 二叉搜索树的范围和
'''


from typing import Optional

from utils.node import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def dfs(node: TreeNode):
            nonlocal res
            if not node:
                return
            v = node.val
            if low <= v <= high:
                res += v
                dfs(node.left)
                dfs(node.right)
            elif v < low:
                dfs(node.right)
            else:
                dfs(node.left)
        dfs(root)
        return res