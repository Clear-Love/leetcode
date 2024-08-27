'''
Author: lmio 2091319361@qq.com
Date: 2024-03-13 18:17:49
LastEditors: lmio 2091319361@qq.com
Description: 2369. 检查数组是否存在有效划分
'''

from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*(n+1)
        dp[0] = True
        dp[2] = nums[1] == nums[0]
        for i in range(3, n+1):
            if dp[i-2] and nums[i-1] == nums[i-2]:
                dp[i] = True
            elif dp[i-3] and nums[i-1] == nums[i-2] == nums[i-3]:
                dp[i] = True
            elif dp[i-3] and nums[i-1] == nums[i-2] + 1 == nums[i-3] + 2:
                dp[i] = True
        return dp[-1]