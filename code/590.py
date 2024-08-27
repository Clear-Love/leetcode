'''
Author: lmio 2091319361@qq.com
Date: 2024-03-19 19:47:39
LastEditors: lmio 2091319361@qq.com
Description: 590. N 叉树的后序遍历
'''

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node: 'Node'):
            if not node:
                return
            for ch in node.children:
                dfs(ch)
            res.append(node.val)
        dfs(root)
        return res