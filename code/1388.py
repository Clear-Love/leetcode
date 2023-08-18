'''
Author: lmio 2091319361@qq.com
Date: 2023-08-18 15:17:33
LastEditors: lmio 2091319361@qq.com
Description: 1388. 3n 块披萨
'''

from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def calc(slices):
            # n向上取整
            N, n = len(slices), (len(slices) + 1) // 3
            # dp[i][j]数组表示0-i中选取j个的最大值
            dp = [[0 for _ in range(n + 1)] for _ in range(N)]
            dp[0][0], dp[0][1] = 0, slices[0]
            dp[1][0], dp[1][1] = 0, max(slices[0], slices[1])
            for i in range(2, N, 1):
                dp[i][0] = 0
                for j in range(1, n+1, 1):
                    # 选或者不选
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + slices[i])
            return dp[N - 1][n]
        ans1 = calc(slices[1:])
        ans2 = calc(slices[0:-1])
        return max(ans1, ans2)