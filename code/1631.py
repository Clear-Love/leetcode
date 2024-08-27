'''
Author: lmio 2091319361@qq.com
Date: 2024-03-06 20:41:48
LastEditors: lmio 2091319361@qq.com
Description: 1631. 最小体力消耗路径
'''

from collections import defaultdict
import heapq
from math import inf
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        vis = set()
        dis = defaultdict(lambda: inf)
        dis[(0, 0)] = 0
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = [(0, (0, 0))]
        while q:
            _, (x, y) = heapq.heappop(q)
            if (x, y) in vis:
                continue
            if (x, y) == (n-1, m-1):
                return dis[(x, y)]
            vis.add((x, y))
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                cost = max(dis[(x, y)], abs(heights[nx][ny]-heights[x][y]))
                if cost <= dis[(nx, ny)]:
                    dis[(nx, ny)] = cost
                    heapq.heappush(q, (dis[(nx, ny)], (nx, ny)))