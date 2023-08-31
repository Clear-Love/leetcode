'''
Author: lmio 2091319361@qq.com
Date: 2023-08-31 18:29:18
LastEditors: lmio 2091319361@qq.com
Description: 1761. 一个图中连通三元组的最小度数
'''

from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [[False for _ in range(n+1)] for _ in range(n+1)]
        degree = [0 for _ in range(n+1)]
        for u, v in edges:
            graph[u][v] = True
            graph[v][u] = True
            degree[u] += 1
            degree[v] += 1
        res = float('inf')
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if not graph[i][j]:
                    continue
                for k in range(j+1, n+1):
                    if graph[i][k] and graph[j][k]:
                        res = min(res, degree[i]+degree[j]+degree[k] - 6)
        return -1 if res == float('inf') else res