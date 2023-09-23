'''
Author: lmio 2091319361@qq.com
Date: 2023-09-21 18:41:24
LastEditors: lmio 2091319361@qq.com
Description: 2603. 收集树中金币
'''

from typing import List


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        graph = [[] for _ in range(n)]
        degree = [0]*n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        q = []
        # 边数
        cnt = n-1
        for i, d in enumerate(degree):
            if d == 1 and coins[i] == 0:
                q.append(i)
        while q:
            cnt -= 1
            index = q.pop()
            degree[index] -= 1
            for x in graph[index]:
                degree[x] -= 1
                if degree[x] == 1 and coins[x] == 0:
                    q.append(x)
        for i, d in enumerate(degree):
            if d == 1:
                q.append(i)
        cnt -= len(q)
        for x in q:
            for y in graph[x]:
                degree[y] -= 1
                if degree[y] == 1:
                    cnt -= 1
        return max(cnt*2, 0)