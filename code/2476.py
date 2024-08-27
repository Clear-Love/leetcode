'''
Author: lmio 2091319361@qq.com
Date: 2024-03-19 21:18:13
LastEditors: lmio 2091319361@qq.com
Description: 2476. 二叉搜索树最近节点查询
'''

import bisect
from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        n = len(arr)
        res = []
        for q in queries:
            i = bisect.bisect_left(arr, q)
            if i == n:
                res.append([arr[i-1], -1])
            elif arr[i] == q:
                res.append([arr[i], arr[i]])
            elif i == 0:
                res.append([-1, arr[i]])
            else:
                res.append([arr[i-1], arr[i]])
        return res