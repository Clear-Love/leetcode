'''
Author: lmio 2091319361@qq.com
Date: 2023-08-24 22:40:34
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.16. 按摩师
'''

from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[1]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]