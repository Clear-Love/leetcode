'''
Author: lmio 2091319361@qq.com
Date: 2023-07-11 16:13:54
LastEditors: lmio 2091319361@qq.com
Description: 并查集
'''
from collections import defaultdict


class unionFind:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(int)
    
    def find(self, x):
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        rank_x, rank_y = self.rank[x], self.rank[y]
        if rank_x > rank_y:
            self.parent[y] = x
        elif rank_x < rank_y:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] += 1