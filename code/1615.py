'''
Author: lmio 2091319361@qq.com
Date: 2023-10-16 23:28:09
LastEditors: lmio 2091319361@qq.com
Description: 1615. 最大网络秩
'''

from itertools import combinations
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0]*n
        graph = set()
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
            neg = (u, v) if u < v else (v, u)
            graph.add(neg)
        res = 0
        for i, j in combinations(range(n), 2):
            rank = degree[i]+degree[j]
            if (i, j) in graph:
                rank -= 1
            res = max(rank, res)
        return res