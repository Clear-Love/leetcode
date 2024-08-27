'''
Author: lmio 2091319361@qq.com
Date: 2024-03-26 17:31:26
LastEditors: lmio 2091319361@qq.com
Description: 518. 零钱兑换 II
'''

from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i: int, c: int) -> int:
            if i < 0:
                return 1 if c == 0 else 0
            if c < coins[i]:
                return dfs(i-1, c)
            return dfs(i-1, c) + dfs(i, c-coins[i])
        return dfs(len(coins)-1, amount)
    
    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x-coin]
        return dp[-1]