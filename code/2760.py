'''
Author: lmio 2091319361@qq.com
Date: 2023-08-02 18:40:26
LastEditors: lmio 2091319361@qq.com
Description: 2760. 最长奇偶子数组
'''

from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        dp = [0] * n
        if nums[0] > threshold:
            dp[0] = 0
        elif nums[0] & 1:
            dp[0] = 0
        else:
            dp[0] = 1
        for i in range(1, n):
            if nums[i] > threshold:
                dp[i] = 0
            elif dp[i-1] == 0 or (nums[i] & 1) ^ (nums[i-1] & 1) == 0:
                dp[i] = 0 if nums[i] & 1 else 1
            else:
                dp[i] = dp[i-1] + 1
        return max(dp)