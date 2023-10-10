'''
Author: lmio 2091319361@qq.com
Date: 2023-10-05 20:34:14
LastEditors: lmio 2091319361@qq.com
Description: 934. 最短的桥
'''

from collections import deque
from itertools import pairwise
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            q.append((i, j))
            grid[i][j] = 2
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)

        n = len(grid)
        dirs = (-1, 0, 1, 0, -1)
        q = deque()
        i, j = next((i, j) for i in range(n) for j in range(n) if grid[i][j])
        dfs(i, j)
        res = 0
        while 1:
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in pairwise(dirs):
                    x, y = i + a, j + b
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return res
                        if grid[x][y] == 0:
                            grid[x][y] = 2
                            q.append((x, y))
            res += 1