'''
Author: lmio 2091319361@qq.com
Date: 2024-05-21 14:16:09
LastEditors: lmio 2091319361@qq.com
Description: 2360. 图中的最长环
'''

from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        deg = [0] * len(edges)
        for v in edges:
            if v != -1:
                deg[v] += 1
        # 记录入度为0的，即起点
        q = [i for i, d in enumerate(deg) if d == 0]
        while q:
            x = q.pop(0)
            y = edges[x]
            if y != -1:
                deg[y] -= 1
                if deg[y] == 0:
                    q.append(y)
        res = -1
        for i in range(len(deg)):
            if deg[i] == 0:
                continue
            ringSize = 0
            while deg[i] != 0:
                deg[i] -= 1
                i = edges[i]
                ringSize += 1
            res = max(res, ringSize)
        return res