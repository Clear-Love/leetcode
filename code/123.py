'''
Author: lmio 2091319361@qq.com
Date: 2023-07-18 18:03:04
LastEditors: lmio 2091319361@qq.com
Description: 123. 买卖股票的最佳时机 III
'''
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(k)] for _ in range(2)] for _ in range(n)]
        dp[0][0] = [-prices[0]] * k
        dp[0][1] = [0] * k
        for i, price in enumerate(prices[1:], start=1):
            dp[i][0][0] = max(dp[i-1][0][0], -price)
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] + price)
            for cnt in range(1, k):
                # 第cnt次买
                dp[i][0][cnt] = max(dp[i-1][0][cnt], dp[i-1][1][cnt-1] - price)
                # 第cnt次卖
                dp[i][1][cnt] = max(dp[i-1][1][cnt], dp[i-1][0][cnt] + price)
        return dp[-1][-1][-1]