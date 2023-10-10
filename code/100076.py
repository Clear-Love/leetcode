'''
Author: lmio 2091319361@qq.com
Date: 2023-10-01 10:55:53
LastEditors: lmio 2091319361@qq.com
Description: 100076. 无限数组的最短子数组
'''

from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        cnt, target = divmod(target, s)
        cnt *= len(nums)
        nums.extend(nums)
        preSum = list(accumulate(nums, initial=0))
        n = len(nums)
        minLen = inf
        left, right = 0, 0
        while right <= n:
            s = preSum[right] - preSum[left]
            if s == target:
                minLen = min(minLen, right-left)
                left += 1
                right = max(left, right)
            elif s < target:
                right += 1
            else:
                left += 1
        return cnt+minLen if minLen != inf else -1