'''
Author: lmio 2091319361@qq.com
Date: 2023-07-15 19:54:36
LastEditors: lmio 2091319361@qq.com
Description: 64. 最小路径和
'''
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp =  [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, n):
            for j in range(1, m):
                v = grid[i][j]
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + v
        return dp[n-1][m-1]