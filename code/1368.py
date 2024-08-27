'''
Author: lmio 2091319361@qq.com
Date: 2024-03-07 18:59:00
LastEditors: lmio 2091319361@qq.com
Description: 1368. 使网格图至少有一条有效路径的最小代价
'''

from collections import defaultdict
import heapq
from math import inf
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(grid), len(grid[0])
        dis = defaultdict(lambda: inf)
        vis = set()
        dis[(0, 0)] = 0
        q = [(0, 0, 0)]
        while q:
            c, x, y = heapq.heappop(q)
            if (x, y) in vis:
                continue
            vis.add((x, y))
            if (x, y) == (n-1, m-1):
                return c
            for i in range(4):
                dx, dy = d[i]
                cost = c+1 if i+1 != grid[x][y] else c
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if cost < dis[(nx, ny)]:
                    dis[(nx, ny)] = cost
                    heapq.heappush(q, (cost, nx, ny))