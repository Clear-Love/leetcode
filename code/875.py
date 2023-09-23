'''
Author: lmio 2091319361@qq.com
Date: 2023-09-18 16:50:23
LastEditors: lmio 2091319361@qq.com
Description: 875. 爱吃香蕉的珂珂
'''

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r) >> 1
            cost = sum([math.ceil(v/mid) for v in piles])
            if cost > h:
                l = mid+1
            else:
                r = mid
        return l