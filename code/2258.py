'''
Author: lmio 2091319361@qq.com
Date: 2023-09-23 17:41:39
LastEditors: lmio 2091319361@qq.com
Description: 2258. 逃离火灾
'''

from collections import deque
import queue
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # 初始火势
        fire_start = [(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == 1]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def check(t: int) ->bool:
            q = fire_start.copy()
            fire = set(fire_start)
            # 火势蔓延
            def next_fire():
                nonlocal q
                tmp = []
                while q:
                    x, y = q.pop()
                    for dx, dy in d:
                        nx, ny = x+dx, y+dy
                        if nx >= 0 and ny >= 0 and nx < n and ny < m and grid[nx][ny] == 0 and (nx, ny) not in fire:
                            fire.add((nx, ny))
                            tmp.append((nx, ny))
                q = tmp
            while t and q:
                next_fire()
                t -= 1
            queue = [(0, 0)]
            vis = set(queue)
            while queue:
                tmp = []
                while queue:
                    x, y = queue.pop()
                    if (x, y) in fire:
                        continue
                    for dx, dy in d:
                        nx, ny = x+dx, y+dy
                        if nx >= 0 and ny >= 0 and nx < n and ny < m and grid[nx][ny] == 0 and (nx, ny) not in vis and (nx, ny) not in fire:
                            if (nx, ny) == (n-1, m-1):
                                return True
                            vis.add((nx, ny))
                            tmp.append((nx, ny))
                queue = tmp
                next_fire()
            return False
        if not check(0):
            return -1
        up = m*n+1
        left, right = 0, up
        while left < right:
            mid = (left+right+1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid-1
        return left if left < up else 10**9