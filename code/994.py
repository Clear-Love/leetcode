'''
Author: lmio 2091319361@qq.com
Date: 2024-05-13 10:10:47
LastEditors: lmio 2091319361@qq.com
Description: 994. 腐烂的橘子
'''

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = []
        for i in range(n):
            for j in range(m):
                # 新鲜橘子加入队列
                if grid[i][j] == 1:
                    q.append((i, j))
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minute = 0
        while q:
            size = len(q)
            update = []
            for _ in range(size):
                x, y = q.pop(0)
                # 周围没有腐烂橘子
                if all([grid[x+dx][y+dy] != 2 for dx, dy in dirs if 0 <= x+dx < n and 0 <= y+dy < m]):
                    q.append((x, y))
                else:
                    update.append((x, y))
            # 没有橘子继续腐烂，返回-1
            if len(q) == size:
                return -1
            for x, y in update:
                grid[x][y] = 2
            minute += 1
        return minute

Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])