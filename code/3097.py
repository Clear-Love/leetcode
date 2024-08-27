'''
Author: lmio 2091319361@qq.com
Date: 2024-04-01 14:28:59
LastEditors: lmio 2091319361@qq.com
Description: 3097. 或值至少为 K 的最短子数组 II
'''

from math import inf
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {}
        res = inf
        for i, num in enumerate(nums):
            d = {v|num:idx for v, idx in d.items()}
            d[num] = i
            for v, idx in d.items():
                if v >= k:
                    res = min(res, i-idx+1)
        return res if res != inf else -1