'''
Author: lmio 2091319361@qq.com
Date: 2023-10-24 19:49:59
LastEditors: lmio 2091319361@qq.com
Description: 1335. 工作计划的最低难度
'''

from functools import cache
from math import inf
from typing import List
    
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        @cache
        def max_range(left: int, right: int) ->int:
            return max(jobDifficulty[left:right])
        @cache
        def dfs(l: int, c: int) ->int:
            if c == 0:
                return max_range(l, n)
            res = inf
            mx = jobDifficulty[l]
            for r in range(l+1, n-c+1):
                res = min(res, mx+dfs(r, c-1))
                mx = max(mx, jobDifficulty[r])
            return res
        return dfs(0, d-1)