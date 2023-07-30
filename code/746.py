'''
Author: lmio 2091319361@qq.com
Date: 2023-07-30 20:51:55
LastEditors: lmio 2091319361@qq.com
Description: 746. 使用最小花费爬楼梯
'''

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]