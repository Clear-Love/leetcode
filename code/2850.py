'''
Author: lmio 2091319361@qq.com
Date: 2023-09-26 16:51:38
LastEditors: lmio 2091319361@qq.com
Description: 2850.将石头分散到网格图的最少移动次数
'''

from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        src = m*n
        dst = src+1
        graph = defaultdict(dict)
        def addEdge(fr: int, to: int, cap: int, cost: int):
            # 正向边
            graph[fr][to] = [cap, cost]
            graph[to][fr] = [0, -cost]
        zeros = [(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == 0]
        # 创建图
        for x, row in enumerate(grid):
            for y, v in enumerate(row):
                if v > 1:
                    key = x*n+y
                    addEdge(src, key, v-1, 0)
                    # 每个大于 1 的格子向每个等于 0 的格子连边，容量为 111，费用为两个格子之间的曼哈顿距离。
                    for i, j in zeros:
                        addEdge(key, i*n+j, 1, abs(x-i)+abs(y-j))
                elif v == 0:
                    addEdge(x*n+y, dst, 1, 0)
        size = m*n+2
        # 路径
        fa = {}
        dist = [inf]*size
        # 最小费最大流模板
        def spfa() ->bool:
            nonlocal dist
            dist = [inf]*size
            dist[src] = 0
            q = deque([src])
            inq = [False]*size
            inq[src] = True
            while q:
                v = q.popleft()
                inq[v] = False
                for to, (cap, cost) in graph[v].items():
                    if not cap:
                        continue
                    nd = dist[v]+cost
                    # 花费更小
                    if nd < dist[to]:
                        dist[to] = nd
                        fa[to] = v
                        if not inq[to]:
                            q.append(to)
                            inq[to] = True
            # 找不到路径则返回False
            return dist[dst] < inf
        def ek() ->(int, int):
            maxFlow, minCost = 0, 0
            while spfa():
                v = dst
                minF = inf
                while v != src:
                    to = fa[v]
                    minF = min(minF, graph[to][v][0])
                    v = to
                v = dst
                while v != src:
                    to = fa[v]
                    e = graph[to][v]
                    e[0] -= minF
                    graph[v][to][0] += minF
                    v = to
                maxFlow += minF
                minCost += dist[dst]*minF
            return maxFlow, minCost
        _, cost = ek()
        return cost