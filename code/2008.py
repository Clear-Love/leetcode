'''
Author: lmio 2091319361@qq.com
Date: 2023-08-20 21:09:07
LastEditors: lmio 2091319361@qq.com
Description: 2008. 出租车的最大盈利
'''

from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        group = [[] for _ in range(n+1)]
        for start, end, tip in rides:
            group[end].append((start, end-start+tip))
        dp = [0]*(n+1)
        res = 0
        for end in range(1, n+1):
            # 不接
            dp[end] = dp[end-1]
            for start, gold in group[end]:
                dp[end] = max(dp[end], dp[start]+gold)
            res = max(res, dp[end])
        return res