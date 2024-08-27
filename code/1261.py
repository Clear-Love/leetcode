'''
Author: lmio 2091319361@qq.com
Date: 2024-03-12 21:50:31
LastEditors: lmio 2091319361@qq.com
Description: 1261. 在受污染的二叉树中查找元素
'''

from typing import Optional

from utils.node import TreeNode


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.mm = set()
        def dfs(node: Optional[TreeNode], x: int):
            if not node:
                return
            node.val = x
            self.mm.add(x)
            dfs(node.left, x*2+1)
            dfs(node.right, x*2+2)
        dfs(root, 0)


    def find(self, target: int) -> bool:
        return target in self.mm