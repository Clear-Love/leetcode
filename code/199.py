'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 13:32:34
LastEditors: lmio 2091319361@qq.com
Description: 199. 二叉树的右视图
'''

from typing import List, Optional

from utils.node import TreeNode

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    h = 0
    res = []
    def dfs(node: TreeNode, level: int):
        nonlocal h
        if not node:
            return
        if level == h:
            res.append(node.val)
            h += 1
        dfs(node.right, level+1)
        dfs(node.left, level+1)
    dfs(root, 0)
    return res