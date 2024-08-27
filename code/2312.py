'''
Author: lmio 2091319361@qq.com
Date: 2024-03-15 23:51:59
LastEditors: lmio 2091319361@qq.com
Description: 2312. 卖木头块
'''

from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            dp[h][w] = p
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i][j],
                              max((dp[i][k] + dp[i][j-k] for k in range(1, j // 2 + 1)), default=0),  # 垂直切割
                              max((dp[k][j] + dp[i-k][j] for k in range(1, i // 2 + 1)), default=0))  # 水平切割
        return dp[m][n]