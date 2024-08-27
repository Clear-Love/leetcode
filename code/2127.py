'''
Author: lmio 2091319361@qq.com
Date: 2024-05-21 10:35:08
LastEditors: lmio 2091319361@qq.com
Description: 2127. 参加会议的最多员工数
'''

from collections import defaultdict
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        degree = [0] * n
        for i, j in enumerate(favorite):
            degree[j] += 1
        q = [i for i, v in enumerate(degree) if v == 0]
        rg = defaultdict(list)
        while q:
            x = q.pop()
            y = favorite[x]
            degree[y] -= 1
            rg[y].append(x)
            if degree[y] == 0:
                q.append(y)
        # 反图最长链
        def dfs(x: int) -> int:
            if not rg[x]:
                return 1
            return max(dfs(y) for y in rg[x])+1
        res = 0
        sumChain = 0
        for i, d in enumerate(degree):
            # 跳过树枝节点
            if d == 0:
                continue
            ringSize = 0
            while degree[i] > 0:
                degree[i] -= 1
                x = favorite[i]
                ringSize += 1
            if ringSize > 2:
                res = max(res, ringSize)
            else:
                sumChain = dfs(i)+dfs(favorite[i])
        return max(res, sumChain)