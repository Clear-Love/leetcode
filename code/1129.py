'''
Author: lmio 2091319361@qq.com
Date: 2023-10-12 22:02:30
LastEditors: lmio 2091319361@qq.com
Description: 1129. 颜色交替的最短路径
'''

from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        graph = [defaultdict(list), defaultdict(list)]
        for i, j in redEdges:
            graph[0][i].append(j)
        for i, j in blueEdges:
            graph[1][i].append(j)
        res = [-1] * n
        vis = set()
        q = deque([(0, 0), (0, 1)])
        d = 0
        while q:
            for _ in range(len(q)):
                i, c = q.popleft()
                if res[i] == -1:
                    res[i] = d
                vis.add((i, c))
                # 颜色交替
                c ^= 1
                for j in graph[c][i]:
                    if (j, c) not in vis:
                        q.append((j, c))
            d += 1
        return res