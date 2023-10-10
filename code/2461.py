'''
Author: lmio 2091319361@qq.com
Date: 2023-09-30 17:50:16
LastEditors: lmio 2091319361@qq.com
Description: 2461. 长度为 K 子数组中的最大和
'''

from typing import Counter, List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnts = Counter(nums[:k])
        s = sum(nums[:k])
        res = s if len(cnts) == k else 0
        left, right = 0, k
        n = len(nums)
        while right < n:
            cnts[nums[right]] += 1
            cnts[nums[left]] -= 1
            s += nums[right]-nums[left]
            if not cnts[nums[left]]:
                cnts.pop(nums[left])
            if len(cnts) == k:
                res = max(res, s)
            left += 1
            right += 1
        return res