'''
Author: lmio 2091319361@qq.com
Date: 2024-03-19 20:03:11
LastEditors: lmio 2091319361@qq.com
Description: 2583. 二叉树中的第 K 大层和
'''


import heapq
from typing import Optional

from utils.node import TreeNode


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        hq = []
        while q:
            tmp = []
            s = 0
            while q:
                node = q.pop()
                s += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if len(hq) < k:
                heapq.heappush(hq, s)
            else:
                if s > hq[0]:
                    heapq.heapreplace(hq, s)
            q = tmp
        if len(hq) < k:
            return -1
        return hq[0]