'''
Author: lmio 2091319361@qq.com
Date: 2023-07-29 15:22:19
LastEditors: lmio 2091319361@qq.com
Description: 872. 叶子相似的树
'''

from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1, l2 = [], []
        def dfs(node: TreeNode, arr: List[int]):
            if not node:
                return
            if not node.left and not node.right:
                arr.append(node.val)
                return
            dfs(node.left, arr)
            dfs(node.right, arr)
        dfs(root1, l1)
        dfs(root2, l2)
        return l1 == l2