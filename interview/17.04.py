'''
Author: lmio 2091319361@qq.com
Date: 2023-08-18 19:34:26
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.04. 消失的数字
'''

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n+1):
            res ^= i
        for num in nums:
            res ^= num
        return res