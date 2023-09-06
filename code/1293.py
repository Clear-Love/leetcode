'''
Author: lmio 2091319361@qq.com
Date: 2023-09-06 09:46:40
LastEditors: lmio 2091319361@qq.com
Description: 1293. 网格中的最短路径
'''

from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque()
        n, m = len(grid), len(grid[0])
        q.append((0, 0, k))
        d = ((0, 1), (0, -1), (-1, 0), (1, 0))
        vis = set()
        if (0, 0) == (n-1, m-1):
            return 0
        step = 0
        while q:
            temp = deque()
            while q:
                x, y, c = q.popleft()
                for dx, dy in d:
                    nx, ny = x+dx, y+dy
                    if (nx, ny, c) in vis:
                        continue
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if grid[nx][ny] == 0:
                        if (nx, ny) == (n-1, m-1):
                            return step+1
                        vis.add((nx, ny, c))
                        temp.append((nx, ny, c))
                    elif c > 0:
                        if (nx, ny) == (n-1, m-1):
                            return step+1
                        vis.add((nx, ny, c))
                        temp.append((nx, ny, c-1))
            step += 1
            q = temp
        return -1