'''
Author: lmio 2091319361@qq.com
Date: 2023-09-16 18:22:12
LastEditors: lmio 2091319361@qq.com
Description: 198. 打家劫舍
'''

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[-1]