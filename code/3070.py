'''
Author: lmio 2091319361@qq.com
Date: 2024-03-04 16:17:11
LastEditors: lmio 2091319361@qq.com
Description: 3070. 元素和小于等于 k 的子矩阵的数目
'''

from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        preSum = [[0 for _ in range(m+1)] for _ in range(n+1)]
        res = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                preSum[i][j] = grid[i-1][j-1] + preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1]
                if preSum[i][j] <= k:
                    res += 1
        return res