'''
Author: lmio 2091319361@qq.com
Date: 2024-03-08 19:17:17
LastEditors: lmio 2091319361@qq.com
Description: 2045. 到达目的地的第二短时间
'''

from collections import deque
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for e in edges:
            x, y = e[0], e[1]
            graph[x].append(y)
            graph[y].append(x)

        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        dist[1][0] = 0
        q = deque([(1, 0)])
        while dist[n][1] == float('inf'):
            p = q.popleft()
            for y in graph[p[0]]:
                d = p[1] + 1
                if d < dist[y][0]:
                    dist[y][0] = d
                    q.append((y, d))
                elif dist[y][0] < d < dist[y][1]:
                    dist[y][1] = d
                    q.append((y, d))

        res = 0
        for _ in range(dist[n][1]):
            if res % (change * 2) >= change:
                res += change * 2 - res % (change * 2)
            res += time
        return res