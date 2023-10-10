'''
Author: lmio 2091319361@qq.com
Date: 2023-09-23 17:09:36
LastEditors: lmio 2091319361@qq.com
Description: 778. 水位上升的泳池中游泳
'''

from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = set()
        def dfs(x: int, y: int, t:int) -> bool:
            vis.add((x, y))
            if grid[x][y] > t:
                return False
            if (x, y) == (n-1, m-1):
                return True
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if (nx, ny) not in vis and nx >= 0 and ny >= 0 and nx < n and ny < m:
                    if dfs(nx, ny, t):
                        return True
            return False
        left, right = 0, max(max(l) for l in grid)
        while left < right:
            mid = (left+right) >> 1
            if dfs(0, 0, mid):
                right = mid
            else:
                left = mid+1
            vis = set()
        return left