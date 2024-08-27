'''
Author: lmio 2091319361@qq.com
Date: 2024-03-18 16:42:53
LastEditors: lmio 2091319361@qq.com
Description: 2813. 子序列最大优雅度
'''

from collections import deque
from typing import List


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: -x[0])
        vis = set()
        dupl = deque()
        total_p = 0
        for p, c in items[:k]:
            total_p += p
            if c not in vis:
                vis.add(c)
            else:
                dupl.append(p)
        res = total_p + len(vis)*len(vis)
        for p, c in items[k:]:
            if c in vis:
                continue
            if dupl:
                total_p += p-dupl.pop()
                vis.add(c)
                res = max(res, total_p+len(vis)*len(vis))
            else:
                break
        return res