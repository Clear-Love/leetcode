'''
Author: lmio 2091319361@qq.com
Date: 2024-03-05 21:46:43
LastEditors: lmio 2091319361@qq.com
Description: 1976. 到达目的地的方案数
'''

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9+7
        g = [[] for _ in range(n)]
        dis = defaultdict(lambda: float("inf"))
        dis[0] = 0
        for x, y, d in roads:
            g[x].append((y, d))
            g[y].append((x, d))
        q = [(0, 0)]
        dp = [float("inf")]*n
        dp[0] = 1
        while q:
            dx, x = heapq.heappop(q)
            if dx > dis[x]:
                continue
            if x == n-1:
                return dp[-1]
            for y, dy in g[x]:
                d = dx + dy
                if d < dis[y]:
                    dis[y] = d
                    dp[y] = dp[x]
                    heapq.heappush(q, (d, y))
                elif d == dis[y]:
                    dp[y] =  (dp[y] + dp[x]) % MOD
        return dp[-1]