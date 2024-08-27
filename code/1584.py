'''
Author: lmio 2091319361@qq.com
Date: 2024-05-27 16:58:25
LastEditors: lmio 2091319361@qq.com
Description: 1584. 连接所有点的最小费用
'''

from typing import List

class setUnion:
    def __init__(self, n: int) -> None:
        self.n = n
        self.rank = [1]*n
        self.f = list(range(n))
    
    def find(self, x: int) -> int:
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def union(self, x: int, y: int) -> None:
        fx, fy = self.find(x), self.find(y)
        if fx == fy: return
        if self.rank[fx] > self.rank[fy]:
            self.f[fy] = fx
        elif self.rank[fx] == self.rank[fy]:
            self.rank[fx] += 1
            self.f[fy] = fx
        else:
            self.f[fx] = fy


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        n = len(points)
        uset = setUnion(n)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                edges.append((dist(i, j), i, j))
        edges.sort()
        res = 0
        num = 1

        for length, x, y in edges:
            if uset.find(x) != uset.find(y):
                uset.union(x, y)
                res += length
                num += 1
                if num == n:
                    break
        return res