'''
Author: lmio 2091319361@qq.com
Date: 2024-03-29 00:17:54
LastEditors: lmio 2091319361@qq.com
Description: 2580. 统计将重叠区间合并成组的方案数
'''

import math
from typing import List


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 1_000_000_000_7
        ranges.sort()
        left, right = 0, 0
        n = len(ranges)
        c = 0
        while right < n:
            r = ranges[left][1]
            while right < n and r >= ranges[right][0]:
                r = max(r, ranges[right][1])
                right += 1
            left = right
            c += 1
        res = 1
        for _ in range(c):
            res = res*2%MOD
        return res