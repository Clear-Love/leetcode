'''
Author: lmio 2091319361@qq.com
Date: 2023-08-10 15:17:45
LastEditors: lmio 2091319361@qq.com
Description: 1289. 下降路径最小和 II
'''

from functools import cache
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[0][j] = grid[0][j]
        for i in range(1, n):
            for j in range(n):
                dp[i][j] = min([num for k, num in enumerate(dp[i-1]) if k != j]) + grid[i][j]
        return min(dp[n-1])