'''
Author: lmio 2091319361@qq.com
Date: 2023-08-02 19:21:44
LastEditors: lmio 2091319361@qq.com
Description: 2762. 不间断子数组
'''

from collections import Counter
from functools import cache
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0
        left = 0
        cnts = Counter()
        for right, v in enumerate(nums):
            cnts[v] += 1
            while max(cnts) - min(cnts) > 2:
                lVal = nums[left]
                cnts[lVal] -= 1
                if cnts[lVal] == 0:
                    del cnts[lVal]
                left += 1
            res += right - left + 1
        return res