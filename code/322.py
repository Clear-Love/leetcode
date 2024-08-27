'''
Author: lmio 2091319361@qq.com
Date: 2024-05-30 16:22:49
LastEditors: lmio 2091319361@qq.com
Description: 322. 零钱兑换
'''

from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        # 组成金额i的最少银币数
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != inf else -1 