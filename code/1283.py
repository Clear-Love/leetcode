'''
Author: lmio 2091319361@qq.com
Date: 2023-09-18 17:01:52
LastEditors: lmio 2091319361@qq.com
Description: 1283.使结果不超过阈值的最小除数
'''

import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            mid = (l+r) >> 1
            if sum([math.ceil(v/mid) for v in nums]) > threshold:
                l = mid+1
            else:
                r = mid
        return l