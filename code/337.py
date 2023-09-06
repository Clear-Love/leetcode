'''
Author: lmio 2091319361@qq.com
Date: 2023-09-02 18:36:25
LastEditors: lmio 2091319361@qq.com
Description: 337. 打家劫舍 III
'''
from functools import cache
from typing import Optional

from utils.node import TreeNode


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> (int, int):
            if not node:
                return 0, 0
            l, ln = dfs(node.left)
            r, rn = dfs(node.right)
            return node.val + ln + rn, max(l, ln) + max(r, rn)
        return max(dfs(root))