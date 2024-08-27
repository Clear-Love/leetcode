'''
Author: lmio 2091319361@qq.com
Date: 2024-03-06 19:05:04
LastEditors: lmio 2091319361@qq.com
Description: 2642. 设计可以求最短路径的图类
'''

from math import inf
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.size = n
        self.d = [[inf]*n for _ in range(n)]
        for i in range(n):
            self.d[i][i] = 0
        for u, v, w in edges:
            self.d[u][v] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])

    def addEdge(self, edge: List[int]) -> None:
        n = self.size
        u, v, w = edge
        if w >= self.d[u][v]:  # 无需更新
            return
        self.d[u][v] = w
        for i in range(n):
            for j in range(n):
                self.d[i][j] = min(self.d[i][j], self.d[i][u] + w + self.d[v][j])
        

    def shortestPath(self, node1: int, node2: int) -> int:
        return self.d[node1][node2] if self.d[node1][node2] != inf else -1