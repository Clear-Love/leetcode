'''
Author: lmio 2091319361@qq.com
Date: 2024-05-08 13:42:23
LastEditors: lmio 2091319361@qq.com
Description: 1463. 摘樱桃 II
'''


from functools import cache
from math import inf
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ds = [(0, 0), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if j >= m or k >= m or j < 0 or k < 0:
                return -inf
            res = -inf
            if i == 0 and (j != 0 or k != m-1):
                return -inf
            if i == 0:
                return grid[i][j] + grid[i][k];
            for d in ds:
                x, y = j + d[0], k + d[1]
                res = max(res, dfs(i-1, x, y))
            res += grid[i][j]
            if j != k:
                res += grid[i][k]
            return res
        ans = 0;
        for j in range(m):
            for k in range(j, m):
                ans = max(ans, dfs(n-1, j, k))
        return ans