'''
Author: lmio 2091319361@qq.com
Date: 2023-10-21 18:14:20
LastEditors: lmio 2091319361@qq.com
Description: 2316. 统计无向图中无法互相到达点对数
'''

from collections import defaultdict, deque
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        vis = set()
        def getLinked(v: int) ->int:
            q = deque([v])
            vis.add(v)
            size = 0
            while q:
                x = q.popleft()
                size += 1
                for y in graph[x]:
                    if y not in vis:
                        q.append(y)
                        vis.add(y)
            return size
        g = []
        s = 0
        for i in range(n):
            if i not in vis:
                g.append(getLinked(i))
                s += g[-1]
        res = 0
        for i in range(len(g)):
            s -= g[i]
            res += g[i]*s
        return res