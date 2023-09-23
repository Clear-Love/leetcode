'''
Author: lmio 2091319361@qq.com
Date: 2023-09-21 19:30:55
LastEditors: lmio 2091319361@qq.com
Description: 1011. 在 D 天内送达包裹的能力
'''

import math
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(w: int) ->bool:
            s = 0
            d = 1
            for v in weights:
                s += v
                if s > w:
                    s = v
                    d += 1
                    if d > days:
                        return False
            return True
        n = len(weights)
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left+right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left