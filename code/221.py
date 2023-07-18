'''
Author: lmio 2091319361@qq.com
Date: 2023-07-18 21:56:24
LastEditors: lmio 2091319361@qq.com
Description: 221. 最大正方形
'''
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        res = 0
        for i in range(n):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                res = 1
        for j in range(m):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                res = 1
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    res = max(dp[i][j], res)
        return res*res