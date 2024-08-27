'''
Author: lmio 2091319361@qq.com
Date: 2024-05-21 16:49:43
LastEditors: lmio 2091319361@qq.com
Description: 1334. 阈值距离内邻居最少的城市
'''

from collections import defaultdict
from functools import cache
from math import inf
from typing import List


# 全源最短路
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[inf]*n for _ in range(n)]
        for u, v, w in edges:
            dp[u][v] = w
            dp[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k]+ dp[k][j])
        res = 0
        min_cnt = inf
        for i in range(n):
            cnt = 0
            for j in range(n):
                if j != i and dp[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= min_cnt:
                min_cnt = cnt
                res = i
        return res