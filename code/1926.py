'''
Author: lmio 2091319361@qq.com
Date: 2023-07-30 15:19:57
LastEditors: lmio 2091319361@qq.com
Description: 1926. 迷宫中离入口最近的出口
'''

from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = deque()
        visited = set()
        visited.add((entrance[0], entrance[1]))
        q.append((entrance[0], entrance[1], 0))
        while q:
            x, y, step = q.popleft()
            if not (x == entrance[0] and y == entrance[1]) and (x == 0 or x == n-1 or y == 0 or y == m-1):
                return step
            for v in d:
                nx, ny = x+v[0], y+v[1]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in visited and maze[nx][ny] == '.':
                    visited.add((nx, ny))
                    q.append((nx, ny, step+1))
        return -1