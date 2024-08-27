'''
Author: lmio 2091319361@qq.com
Date: 2024-03-16 15:40:13
LastEditors: lmio 2091319361@qq.com
Description: 2684. 矩阵中移动的最大次数
'''

from functools import cache
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        d = [(-1, 1), (0, 1), (1, 1)]

        @cache
        def dfs(x: int, y: int) -> int:
            ans = 0
            v = grid[x][y]
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny] > v:
                    ans = max(ans, 1+dfs(nx, ny))
            return ans
        return max(dfs(x, 0) for x in range(n))
