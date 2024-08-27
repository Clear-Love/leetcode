'''
Author: lmio 2091319361@qq.com
Date: 2024-04-08 17:10:45
LastEditors: lmio 2091319361@qq.com
Description: 2009. 使数组连续的最少操作数
'''
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        left = 0
        res = 0
        for i, num in enumerate(nums):
            while left< n and nums[left] < num-n+1:
                left += 1
            res = max(res, i-left+1)
        return n-res