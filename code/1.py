'''
Author: lmio 2091319361@qq.com
Date: 2023-07-15 02:43:53
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, v in enumerate(nums):
            y = target - v
            if y in m:
                return [m[y], i]
            m[v] = i