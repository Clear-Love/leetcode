'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 16:36:27
LastEditors: lmio 2091319361@qq.com
Description: 2500. 删除每行中的最大值
'''
import heapq
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            grid[i].sort(reverse=True)
        res = 0
        for _ in range(m):
            maxVal = float('-inf')
            for j in range(n):
                maxVal = max(maxVal, grid[j].pop())
            res += maxVal
        return res