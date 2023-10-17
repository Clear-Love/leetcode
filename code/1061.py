'''
Author: lmio 2091319361@qq.com
Date: 2023-10-17 20:59:45
LastEditors: lmio 2091319361@qq.com
Description: 1061. 按字典序排列最小的等效字符串
'''

from collections import defaultdict
from functools import cache


class unionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x: str):
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x: str, y: str):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if x > y:
            self.parent[x] = y
        else:
            self.parent[y] = x

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = unionFind()
        for i in range(len(s1)):
            uf.union(s1[i], s2[i])
        res = []
        @cache
        def f(ch: str) -> str:
            return uf.find(ch)
        for ch in baseStr:
            res.append(f(ch))
        return ''.join(res)