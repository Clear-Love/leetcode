'''
Author: lmio 2091319361@qq.com
Date: 2023-10-05 20:05:32
LastEditors: lmio 2091319361@qq.com
Description: 309. 买卖股票的最佳时机含冷冻期
'''

from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0, dp1, dp2 = 0, -inf, -prices[0]
        for i in range(1, len(prices)):
            dp0, dp1, dp2 = max(dp0, dp1), dp2 + prices[i], max(dp2, dp0 - prices[i])   
        return max(dp0, dp1, dp2)