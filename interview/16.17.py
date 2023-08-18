'''
Author: lmio 2091319361@qq.com
Date: 2023-08-16 21:05:18
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.17. 连续数列
'''

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        last = nums[0]
        res = last
        for i in range(1, len(nums)):
            last = max(nums[i], last + nums[i])
            res = max(res, last)
        return res