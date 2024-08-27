'''
Author: lmio 2091319361@qq.com
Date: 2024-05-27 18:25:25
LastEditors: lmio 2091319361@qq.com
Description: 1489. 找到最小生成树里的关键边和伪关键边
'''

from typing import List

class setUnion:
    def __init__(self, n: int) -> None:
        self.n = n
        self.rank = [1]*n
        self.f = list(range(n))
        # 当前连通分量数目
        self.setCount = n
    
    def find(self, x: int) -> int:
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy: return False
        if self.rank[fx] > self.rank[fy]:
            self.f[fy] = fx
        elif self.rank[fx] == self.rank[fy]:
            self.rank[fx] += 1
            self.f[fy] = fx
        else:
            self.f[fx] = fy
        self.setCount -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        value = 0
        unset = setUnion(n)
        for i in range(m):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])
        for u, v, w, i in edges:
            if unset.union(u, v):
                value += w
        
        
        # 关键边数目，伪关键边数目
        res = [[], []]
        
        for i in range(m):
            # 判断是否是关键边
            uf = setUnion(n)
            v = 0
            for j in range(m):
                if j != i and uf.union(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            # 无法得到最小生成树或者得到最小生成树但是权重变大了
            if uf.setCount != 1 or (uf.setCount == 1 and v > value):
                res[0].append(edges[i][3])
                continue

            # 判断是否是伪关键边
            uf = setUnion(n)
            uf.union(edges[i][0], edges[i][1])
            v = edges[i][2]
            for j in range(m):
                if j != i and uf.union(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if v == value:
                res[1].append(edges[i][3])
        return res