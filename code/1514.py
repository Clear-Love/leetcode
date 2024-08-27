'''
Author: lmio 2091319361@qq.com
Date: 2024-03-06 20:19:58
LastEditors: lmio 2091319361@qq.com
Description: 1514. 概率最大的路径
'''

from collections import defaultdict
import heapq
from math import inf
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            g[u].append((v, p))
            g[v].append((u, p))
        prob = [inf]*n
        prob[start_node] = 1
        vis = set()
        q = [(-1, start_node)]
        while q:
            px, x = heapq.heappop(q)
            if x in vis:
                continue
            if x == end_node:
                return -prob[x]
            for y, py in g[x]:
                p = px*py
                if p < prob[y]:
                    prob[y] = p
                    heapq.heappush(q, (p, y))
        return 0