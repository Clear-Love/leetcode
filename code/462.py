'''
Author: lmio 2091319361@qq.com
Date: 2024-03-13 21:53:27
LastEditors: lmio 2091319361@qq.com
Description: 462. 最小操作次数使数组元素相等 II
'''

from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n & 1 == 0:
            v = (nums[n//2] + nums[n//2+1])//2
        else:
            v = nums[n//2]
        return sum(abs(x-v) for x in nums)