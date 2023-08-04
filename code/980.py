'''
Author: lmio 2091319361@qq.com
Date: 2023-08-04 21:05:06
LastEditors: lmio 2091319361@qq.com
Description: 980. 不同路径 III
'''

from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        visited = set()
        d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def dfs(x: int, y: int):
            nonlocal res
            if grid[x][y] == 2 and len(visited) == cnt:
                res += 1
                return
            visited.add((x, y))
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny] != -1 and (nx, ny) not in visited:
                    dfs(nx, ny)
            visited.remove((x, y))
        x, y = 0, 0
        cnt = 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    cnt += 1
        dfs(x, y)
        return 0