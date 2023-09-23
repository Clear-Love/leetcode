'''
Author: lmio 2091319361@qq.com
Date: 2023-09-21 19:53:52
LastEditors: lmio 2091319361@qq.com
Description: 2064. 分配给商店的最多商品的最小值
'''

import math
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(c: int) ->bool:
            r = n
            for q in quantities:
                r -= math.ceil(q/c)
                if r < 0:
                    return False
            return True
        left, right = 1, max(quantities)+1
        while left < right:
            mid = (left+right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left