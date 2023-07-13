'''
Author: lmio 2091319361@qq.com
Date: 2023-07-13 20:57:58
LastEditors: lmio 2091319361@qq.com
Description: 931. 下降路径最小和
'''
from typing import List

class Solution:
    def minFallingPathSum(matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        dp = []*n
        def maxdp(i: int) -> int:
            left = max(i-1, 0)
            right = min(i+1, n)
            return max(dp[left], dp[i], dp[right])
        for i in range(n):
            dp[i] = matrix[0][i]
        for i in range(1, len(matrix)):
            tmp = []
            for j in range(len(matrix[i])):
                tmp[j] = matrix[i][j] + maxdp(j)
            dp = tmp
        return max(dp)