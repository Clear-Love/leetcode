'''
Author: lmio 2091319361@qq.com
Date: 2024-03-19 19:39:53
LastEditors: lmio 2091319361@qq.com
Description: 589. N 叉树的前序遍历
'''


from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node: 'Node'):
            if not node:
                return
            res.append(node.val)
            for ch in node.children:
                dfs(ch)
        dfs(root)
        return res