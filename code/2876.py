'''
Author: lmio 2091319361@qq.com
Date: 2023-10-02 14:31:09
LastEditors: lmio 2091319361@qq.com
Description: 2876. 有向图访问计数
tag: 内向基环树, 拓扑排序
'''

from collections import deque
from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        rg = [[] for _ in range(n)] # 反图
        deg = [0]*n # 入度表
        for i, to in enumerate(edges):
            rg[to].append(i)
            deg[to] += 1
        q = deque([i for i, v in enumerate(deg) if v == 0])
        while q:
            v = q.popleft()
            to = edges[v]
            deg[to] -= 1
            if deg[to] == 0:
                q.append(to)
        res = [0]*n
        # 在反图上遍历树枝
        def rdfs(x: int, depth: int) -> None:
            res[x] = depth
            for y in rg[x]:
                # 进入树枝
                if deg[y] == 0:  # 树枝上的点在拓扑排序后，入度均为 0
                    rdfs(y, depth + 1)
        for i, d in enumerate(deg):
            # 取出不在基环中的点
            if d <= 0:
                continue
            x = i
            ring = []
            # 基环内的点入度为-1，防止重复
            while True:
                ring.append(x)
                deg[x] = -1
                x = edges[x]
                if x == i:
                    break
            for x in ring:
                rdfs(x, len(ring))
        return res