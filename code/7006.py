'''
Author: lmio 2091319361@qq.com
Date: 2023-08-20 10:56:56
LastEditors: lmio 2091319361@qq.com
Description: 7006. 销售利润最大化
'''

import bisect
from functools import cache
from typing import List


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # groups = [[] for _ in range(n)]
        # for start, end, gold in offers:
        #     groups[end].append((start, gold))
        # dp = [0] * (n + 1)
        # for end, g in enumerate(groups):
        #     # 不选
        #     dp[end+1] = dp[end]
        #     for start, gold in g:
        #         dp[end + 1] = max(dp[end + 1], dp[start] + gold)
        # return dp[n]
        offers.sort(key=lambda x: x[1])
        n = len(offers)
        dp = [0]*(n+1)
        for i, (start, _, gold) in enumerate(offers, start=1):
            j = bisect.bisect_right(offers, start-1, hi=i, key=lambda x: x[1])
            dp[i] = max(dp[i-1], dp[j] + gold)
        return dp[-1]