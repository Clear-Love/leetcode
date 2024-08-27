'''
Author: lmio 2091319361@qq.com
Date: 2024-05-06 15:18:46
LastEditors: lmio 2091319361@qq.com
Description: 741. 摘樱桃
'''

from functools import cache
from math import inf
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 走了t步，a横向走i步，b横向走j步
        @cache
        def dfs(t: int, i: int, j: int) ->int:
            if i < 0 or j < 0 or t < i or t < j or grid[i][t-i] < 0 or grid[j][t-j] < 0:
                return -inf
            if t == 0:
                return grid[0][0]
            res = max(dfs(t-1, i, j-1), dfs(t-1, i-1, j-1), dfs(t-1, i-1, j), dfs(t-1, i, j))
            res += grid[i][t-i]
            if i != j:
                res += grid[j][t-j]
            return res
        return max(dfs(n*2-2, n-1, n-1), 0)