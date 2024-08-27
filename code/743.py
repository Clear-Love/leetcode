'''
Author: lmio 2091319361@qq.com
Date: 2024-03-06 18:53:41
LastEditors: lmio 2091319361@qq.com
Description: 743. 网络延迟时间
'''

from collections import defaultdict
import heapq
from math import inf
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u, v, d in times:
            g[u].append((v, d))
        dis = [inf]*(n+1)
        dis[0] = 0
        dis[k] = 0
        vis = set()
        q = [(0, k)]
        while q:
            dx, x = heapq.heappop(q)
            if x in vis:
                continue
            vis.add(x)
            for y, dy in g[x]:
                d = dx+dy
                if d < dis[y]:
                    dis[y] = d
                    heapq.heappush(q, (d, y))
        if len(vis) != n:
            return -1
        return max(dis)