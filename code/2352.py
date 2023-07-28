'''
Author: lmio 2091319361@qq.com
Date: 2023-07-28 14:09:48
LastEditors: lmio 2091319361@qq.com
Description: 2352. 相等行列对
'''
from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        cnt = Counter(tuple(row) for row in grid)
        res = 0
        for j in range(len(grid[0])):
            res += cnt[tuple([grid[i][j] for i in range(len(grid[0]))])]
        return res