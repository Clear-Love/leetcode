'''
Author: lmio 2091319361@qq.com
Date: 2024-05-12 10:48:26
LastEditors: lmio 2091319361@qq.com
Description: 100281. 矩阵中的最大得分
'''

from math import inf
from typing import List

# 给你一个由 正整数 组成、大小为 m x n 的矩阵 grid。你可以从矩阵中的任一单元格移动到另一个位于正下方或正右侧的任意单元格（不必相邻）。从值为 c1 的单元格移动到值为 c2 的单元格的得分为 c2 - c1 。
# 你可以从 任一 单元格开始，并且必须至少移动一次。
# 返回你能得到的 最大 总得分。
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        preMin = [[0] * (m) for _ in range(n)]
        preMin[0][0] = grid[0][0]
        for i in range(1, n):
            preMin[i][0] = min(preMin[i-1][0], grid[i][0])
        for j in range(1, m):
            preMin[0][j] = min(preMin[0][j-1], grid[0][j])
        for i in range(1, n):
            for j in range(1, m):
                preMin[i][j] = min(preMin[i-1][j], preMin[i][j-1], grid[i][j])
        res = -inf
        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    res = max(res, grid[i][j] - min(preMin[i-1][j], preMin[i][j-1]))
                elif i > 0:
                    res = max(res, grid[i][j] - preMin[i-1][j])
                elif j > 0:
                    res = max(res, grid[i][j] - preMin[i][j-1])
        return res