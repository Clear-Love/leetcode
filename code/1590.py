'''
Author: lmio 2091319361@qq.com
Date: 2023-08-18 23:08:26
LastEditors: lmio 2091319361@qq.com
Description: 1590. 使数组和能被 P 整除
'''

from itertools import accumulate
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        preSum = list(accumulate(nums))
        res = len(nums)
        m = {}
        m[0] = 1
        gap = preSum[-1] % p
        for i, s in enumerate(preSum):
            mod = (s-gap)%p
            if mod in m:
                res = min(res, i-m[mod]+1) 
            m[mod] = i
        if res == len(nums):
            return -1
        return res