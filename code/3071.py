'''
Author: lmio 2091319361@qq.com
Date: 2024-03-04 22:24:52
LastEditors: lmio 2091319361@qq.com
Description: 3071. 在矩阵上写出字母 Y 所需的最少操作次数
'''

from collections import defaultdict
from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        mid = m//2
        cnt_y = defaultdict(int)
        cnts = defaultdict(int)
        c = 0
        for i in range(n):
            for j in range(m):
                if (i == j and j <= mid) or (i == m-j-1 and j > mid) or (j == mid and i >= mid):
                    cnt_y[grid[i][j]] += 1
                    c += 1
                else:
                    cnts[grid[i][j]] += 1
        res = n*m
        for x in range(3):
            v = cnts[x]
            cnts[x] = 0
            res = min(res, c-cnt_y[x] + n*m-c-max(cnts.values()))
            cnts[x] = v
        return res

print(Solution().minimumOperationsToWriteY([[1,2,2],[1,1,0],[0,1,0]]))