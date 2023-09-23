'''
Author: lmio 2091319361@qq.com
Date: 2023-09-17 19:09:31
LastEditors: lmio 2091319361@qq.com
Description: 2596. 检查骑士巡视方案
'''

from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        pos = [[] for _ in range(n*n)]
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = (j, i)
        if pos[0] != (0, 0):
            return False
        for i in range(1, len(pos)):
            x1, y1 = pos[i-1]
            x2, y2 = pos[i]
            dx, dy = abs(x1-x2), abs(y1-y2)
            if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
                continue
            return False
        return True