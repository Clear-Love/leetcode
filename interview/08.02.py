'''
Author: lmio 2091319361@qq.com
Date: 2023-08-07 14:11:17
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.02. 迷路的机器人
'''

from typing import List


class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[False for _ in range(m)] for _ in range(n)]
        dp[0][0] = obstacleGrid[0][0] == 0
        for j in range(1, m):
            dp[0][j] = obstacleGrid[0][j] == 0 and dp[0][j-1]
        for i in range(1, n):
            dp[i][0] = obstacleGrid[i][0] == 0 and dp[i-1][0]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = obstacleGrid[i][j] == 0 and (dp[i][j-1] or dp[i-1][j])
    
        if not dp[n-1][m-1]:
            return []
        d = [(0, -1),(-1, 0)]
        x, y = n-1, m-1
        res = [[x, y]]
        while not(x == 0 and y == 0):
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx >=0 and ny >= 0 and dp[nx][ny]:
                    res.append([nx, ny])
                    x, y = nx, ny
                    break
        res.reverse()
        return res