'''
Author: lmio 2091319361@qq.com
Date: 2023-10-12 22:02:30
LastEditors: lmio 2091319361@qq.com
Description: 1129. 颜色交替的最短路径
'''

from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for i, j in redEdges:
            g[i].append((j, 0))
        for i, j in blueEdges:
            g[i].append((j, 1))
        res = [-1] * n
        vis = set()
        q = deque([(0, -1, 0)])
        while q:
            i, color, d = q.popleft()
            if (i, color) in vis:
                continue
            vis.add((i, color))
            if res[i] == -1 or d < res[i]:
                res[i] = d
            for j, c in g[i]:
                if c != color:
                    q.append((j, c, d+1))
        return res