'''
Author: lmio 2091319361@qq.com
Date: 2023-09-06 08:59:15
LastEditors: lmio 2091319361@qq.com
Description: 1123. 最深叶节点的最近公共祖先
'''

from typing import Optional
from utils.node import TreeNode

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = None
        max_depth = -1  # 全局最大深度
        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal res, max_depth
            if node is None:
                max_depth = max(max_depth, depth)  # 维护全局最大深度
                return depth
            left_max_depth = dfs(node.left, depth + 1)  # 获取左子树最深叶节点的深度
            right_max_depth = dfs(node.right, depth + 1)  # 获取右子树最深叶节点的深度
            if left_max_depth == right_max_depth == max_depth:
                res = node
            return max(left_max_depth, right_max_depth)  # 当前子树最深叶节点的深度
        dfs(root, 0)
        return res