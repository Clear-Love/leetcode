'''
Author: lmio 2091319361@qq.com
Date: 2024-03-07 21:58:08
LastEditors: lmio 2091319361@qq.com
Description: 1786. 从第一个节点出发到最后一个节点的受限路径数
'''

from collections import defaultdict
import heapq
from math import inf
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9+7
        dis = [inf]*(n+1)
        dis[n] = 0
        g = defaultdict(dict)
        for u, v, d in edges:
            g[u][v] = d
            g[v][u] = d
        vis = set()
        q = [(0, n)]
        cnt = [0]*(n+1)
        cnt[n] = 1
        while q:
            dx, x = heapq.heappop(q)
            if x in vis:
                continue
            vis.add(x)
            for y in g[x]:
                d = dx+g[x][y]
                if d < dis[y]:
                    dis[y] = d
                    heapq.heappush(q, (d, y))
                if dis[y] > dis[x]:
                    cnt[y] = (cnt[x] + cnt[y])%MOD
        return cnt[1]