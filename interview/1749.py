'''
Author: lmio 2091319361@qq.com
Date: 2023-08-08 15:54:13
LastEditors: lmio 2091319361@qq.com
Description: 1749. 任意子数组和的绝对值的最大值
'''

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # s = list(accumulate(nums, initial=0)) # nums 的前缀和
        # return max(s) - min(s)
        n = len(nums)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        # dp[i][0] 以nums[i]结尾且和小于零
        if nums[0] < 0:
            dp[0][0] = nums[0]
        else:
            dp[0][1] = nums[0]
        res = max(abs(dp[0][0]), abs(dp[0][1]))
        for i in range(1, n):
            v = nums[i]
            if dp[i-1][0] + v < 0:
                dp[i][0] = dp[i-1][0] + v
            if dp[i-1][1] + v >= 0:
                dp[i][1] = dp[i-1][1] + v
            res = max(res, abs(dp[i][0]), abs(dp[i][1]))
        return res