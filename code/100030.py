'''
Author: lmio 2091319361@qq.com
Date: 2023-09-10 11:10:52
LastEditors: lmio 2091319361@qq.com
Description: 100030. 将石头分散到网格图的最少移动次数
'''

from collections import deque
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        l = []
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        cnts = {}
        for i in range(3):
            for j in range(3):
                if grid[i][j] > 1:
                    l.append((i, j, 0, i*3+j))
                    cnts[i*3+j] = grid[i][j]-1
                    grid[i][j] = 1
        queue = deque(sorted(l, key=lambda x: -cnts[x[3]]))
        visited = set()
        while queue:
            x, y, s, id = queue.popleft()
            if cnts[id] == 0:
                continue
            if grid[x][y] == 0:
                grid[x][y] = 1
                cnts[id] -= 1
                res += s
                if cnts[id] == 0:
                    continue
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx >= 0 and ny >=0 and nx < 3 and ny < 3 and (nx, ny, id) not in visited:
                    visited.add((nx, ny, id))
                    queue.append((nx, ny, s+1, id))
        return res