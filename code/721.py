'''
Author: lmio 2091319361@qq.com
Date: 2023-10-17 16:04:00
LastEditors: lmio 2091319361@qq.com
Description: 721. 账户合并
'''

from collections import defaultdict
from typing import List

class unionFind:
    def __init__(self) -> None:
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

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        uf = unionFind()
        res = defaultdict(list)
        for account in accounts:
            name = account[0]
            n = len(account)
            for i in range(1, n):
                email_to_name[account[i]] = name
                if i+1 < n:
                    uf.union(account[i], account[i+1])
        for email in email_to_name.keys():
            res[uf.find(email)].append(email)
        return [[email_to_name[k]] + sorted(v) for k, v in res.items()]