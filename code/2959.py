'''
Author: lmio 2091319361@qq.com
Date: 2024-05-24 19:59:08
LastEditors: lmio 2091319361@qq.com
Description: 2959. 关闭分部的可行集合数目
'''

from math import inf
from typing import List


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        def check(q: set) -> bool:
            d = [[inf] * n for _ in range(n)]
            for i in range(n):
                d[i][i] = 0
            for u, v, w in roads:
                if u in q or v in q:
                    continue
                d[u][v] = min(w, d[u][v])
                d[v][u] = min(w, d[v][u])
            # floyd算法
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            mm = set(range(n))-q
            for i in mm:
                for j in mm:
                    if d[i][j] > maxDistance:
                        return False
            return True
        
        m = set()
        res = 0
        if check(m):
            res += 1
        def dfs(i: int):
            nonlocal res
            if check(m):
                res += 1
            for j in range(i+1, n):
                m.add(j)
                dfs(j)
                m.remove(j)
        for i in range(n):
            m.add(i)
            dfs(i)
            m.remove(i)
        return res