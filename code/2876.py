'''
Author: lmio 2091319361@qq.com
Date: 2023-10-02 14:31:09
LastEditors: lmio 2091319361@qq.com
Description: 2876. 有向图访问计数
tag: 内向基环树, 拓扑排序
'''

from collections import defaultdict, deque
from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        deg = [0]*n
        for v in edges:
            deg[v] += 1
        q = [i for i in range(n) if deg[i] == 0]
        # 反图
        rg = defaultdict(list)
        while q:
            x = q.pop()
            y = edges[x]
            rg[y].append(x)
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)
        res = [0]*n
        def dfs(x: int, cnt: int):
            res[x] = cnt
            for y in rg[x]:
                dfs(y, cnt+1)
        for i in range(n):
            if deg[i] == 0:
                continue
            ringSize = 0
            rings = []
            while deg[i] > 0:
                deg[i] -= 1
                ringSize += 1
                rings.append(i)
                i = edges[i]
            for y in rings:
                dfs(y, ringSize)
        return res