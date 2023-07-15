'''
Author: lmio 2091319361@qq.com
Date: 2023-07-14 21:32:40
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from typing import Optional

from utils.node import TreeNode


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            d = dfs(node.left) + dfs(node.right) + node.val - 1
            nonlocal res
            res += abs(d)
            return d
        dfs(root)
        return res