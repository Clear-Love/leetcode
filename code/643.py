'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 20:45:58
LastEditors: lmio 2091319361@qq.com
Description: 643. 子数组最大平均数 I
'''

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        kSum = sum(nums[:k])
        left, right = 1, k
        res = kSum/k
        while right < len(nums):
            kSum -= nums[left-1]
            kSum += nums[right]
            res = max(res, kSum/k)
            left += 1
            right += 1
        return res