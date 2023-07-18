'''
Author: lmio 2091319361@qq.com
Date: 2023-07-15 20:37:22
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp =  [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = obstacleGrid[0][0]^1
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] & (obstacleGrid[0][j]^1)
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] & (obstacleGrid[i][0]^1)
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[n-1][m-1]