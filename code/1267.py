'''
Author: lmio 2091319361@qq.com
Date: 2023-08-24 15:17:20
LastEditors: lmio 2091319361@qq.com
Description: 1267. 统计参与通信的服务器
'''

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        row = [0]*n
        col = [0]*m
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    if row[i] == 1 and col[j] == 1:
                        continue
                    res += 1
        return res