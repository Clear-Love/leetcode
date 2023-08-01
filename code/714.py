'''
Author: lmio 2091319361@qq.com
Date: 2023-07-31 15:44:59
LastEditors: lmio 2091319361@qq.com
Description: 714. 买卖股票的最佳时机含手续费
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp[i][0] 第i天未持有股票的最大利润
        # dp[i][1] 第i天持有股票的最大利润
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]-fee
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - fee - prices[i], dp[i-1][1])
        return dp[-1][0]