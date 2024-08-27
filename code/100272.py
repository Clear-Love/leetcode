'''
Author: lmio 2091319361@qq.com
Date: 2024-03-30 22:34:36
LastEditors: lmio 2091319361@qq.com
Description: 100272. 或值至少 K 的最短子数组 I
'''

from typing import List

from torch import le


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = n+1
        left, right = 0, 1
        while left < n:
            s = nums[left]
            v = 0
            while right < n and s < k:
                s |= nums[right]
                right += 1
                v = max(v, nums[right])
            if s < k:
                return
            res = min(res, right-left)
            while nums[left] < v:
                left += 1
            right = left+1
        return res if res <= n else -1