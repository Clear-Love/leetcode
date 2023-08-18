'''
Author: lmio 2091319361@qq.com
Date: 2023-08-17 18:45:51
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.19. 水域大小
'''
from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        n, m = len(land), len(land[0])
        res = []
        visited = set()
        d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        def dfs(x: int, y: int):
            visited.add((x, y))
            size = 1
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and land[nx][ny] == 0 and (nx, ny) not in visited:
                    size += dfs(nx, ny)
            return size
        for i in range(n):
            for j in range(m):
                if land[i][j] == 0 and (i, j) not in visited:
                    res.append(dfs(i, j))
        res.sort()
        return res