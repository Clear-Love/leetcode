'''
Author: lmio 2091319361@qq.com
Date: 2023-10-18 22:31:54
LastEditors: lmio 2091319361@qq.com
Description: 1857. 有向图中最大颜色值
'''

from collections import deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        anti = [[] for _ in range(n)]
        deg = [0]*n
        for u, v in edges:
            graph[u].append(v)
            anti[v].append(u)
            deg[v] += 1
        q = deque(i for i, v in enumerate(deg) if v == 0)
        vis = n
        dp = [[0]*26 for _ in range(n)]
        res = 0
        while q:
            x = q.popleft()
            vis -= 1
            dp[x][ord(colors[x])-97] += 1
            res = max(res, dp[x][ord(colors[x])-97])
            for y in graph[x]:
                deg[y] -= 1
                for i in range(26):
                    dp[y][i] = max(dp[y][i], dp[x][i])
                if not deg[y]:
                    q.append(y)
        if vis:
            return -1
        return res