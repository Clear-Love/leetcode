'''
Author: lmio 2091319361@qq.com
Date: 2024-03-07 20:12:15
LastEditors: lmio 2091319361@qq.com
Description: LCP 56. 信物传送
'''

from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:
    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        front = {'^': 0, 'v': 1, '<': 2, '>': 3}
        n, m = len(matrix), len(matrix[0])
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dis = defaultdict(lambda: inf)
        dis[(start[0], start[1])] = 0
        vis = set()
        q = deque([(start[0], start[1])])
        while q:
            x, y = q.popleft()
            if (x, y) in vis:
                continue
            vis.add((x, y))
            if (x, y) == (end[0], end[1]):
                return dis[(x, y)]
            for i in range(4):
                dx, dy = d[i]
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                cost = dis[(x, y)]+1 if i != front[matrix[x][y]] else dis[(x, y)]
                if cost < dis[(nx, ny)]:
                    dis[(nx, ny)] = cost
                    if i != front[matrix[x][y]]:
                        q.append((nx, ny))
                    else:
                        q.appendleft((nx, ny))