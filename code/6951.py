'''
Author: lmio 2091319361@qq.com
Date: 2023-08-06 11:14:13
LastEditors: lmio 2091319361@qq.com
Description: 6951. 找出最安全路径
'''

from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        thiefs = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    thiefs.append((i, j))
        res = 0
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def dfs(x: int, y: int, val: int):
            nonlocal res
            for i, j in thiefs:
                val = min(val, abs(x -i) + abs(y -j))
            if x == n-1 and y == n-1:
                res = max(res, val)
                return
            if grid[x][y] == 1 or val <= res:
                return
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dfs(nx, ny, val)
                    visited.remove((nx, ny))
        dfs(0, 0, float('inf'))
        return res