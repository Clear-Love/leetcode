'''
Author: lmio 2091319361@qq.com
Date: 2024-03-08 14:49:50
LastEditors: lmio 2091319361@qq.com
Description: 2662. 前往目标的最小代价
'''

from collections import defaultdict
import heapq
from math import inf
from typing import List


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        g = defaultdict(lambda: defaultdict(lambda: inf))
        startx, starty = start
        endx, endy = target
        q = [(0, startx, starty)]
        roads = [(endx, endy)]
        vis = set()
        dis = defaultdict(lambda: inf)
        dis[(startx, starty)] = 0
        for x1, y1, x2, y2, cost in specialRoads:
            g[(x1, y1)][(x2, y2)] = min(g[(x1, y1)][(x2, y2)], cost)
            roads.append((x1, y1))
        while q:
            c, x1, y1 = heapq.heappop(q)
            if (x1, y1) in vis:
                continue
            if (x1, y1) == (endx, endy):
                return c
            vis.add((x1, y1))
            for x2, y2 in g[(x1, y1)]:
                cost = c + g[(x1, y1)][(x2, y2)]
                if cost < dis[(x2, y2)]:
                    dis[(x2, y2)] = cost
                    heapq.heappush(q, (cost, x2, y2))
            for x2, y2 in roads:
                cost = c + abs(x1-x2) + abs(y1-y2)
                if cost < dis[(x2, y2)]:
                    dis[(x2, y2)] = cost
                    heapq.heappush(q, (cost, x2, y2))

print(Solution().minimumCost([1, 1], [4, 5], [[1, 2,3,3,2],[3,4,4,5,1]]))