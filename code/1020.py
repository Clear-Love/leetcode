'''
Author: lmio 2091319361@qq.com
Date: 2023-10-08 23:06:58
LastEditors: lmio 2091319361@qq.com
Description: 1020. 飞地的数量
'''

from collections import deque
from itertools import pairwise
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = set()
        q = deque()
        res = sum(map(sum,grid))
        for i in range(m):
            for j in  range(n):
                if (i in (0,m - 1) or j in (0,n - 1)) and grid[i][j] == 1:
                    vis.add((i, j))
                    q.append((i, j))
                    res -= 1
        while q:
            r, c = q.popleft()
            for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x, y) not in vis:
                    vis.add((x, y))
                    q.append((x, y))
                    res -= 1
        return res