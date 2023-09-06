'''
Author: lmio 2091319361@qq.com
Date: 2023-09-04 10:47:05
LastEditors: lmio 2091319361@qq.com
Description: 740. 删除并获得点数
'''

from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        nums = sorted(list(cnts.keys()))
        n = len(nums)
        dp = [0  for _ in range(n+1)]
        dp[1] = nums[0] * cnts[nums[0]]
        for i in range(2, n+1):
            if nums[i-1] - nums[i-2] == 1:
                dp[i] = max(dp[i-1], nums[i-1]*cnts[nums[i-1]] + dp[i-2])
            else:
                dp[i] = nums[i-1]*cnts[nums[i-1]] + dp[i-1]
        return dp[-1]