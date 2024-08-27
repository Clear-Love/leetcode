'''
Author: lmio 2091319361@qq.com
Date: 2024-03-19 19:26:42
LastEditors: lmio 2091319361@qq.com
Description: 429. N 叉树的层序遍历
'''
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            tmp = deque()
            arr = []
            while q:
                node = q.popleft()
                arr.append(node.val)
                for ch in node.children:
                    tmp.append(ch)
            res.append(arr.copy())
            q = tmp
        return res