'''
Author: lmio 2091319361@qq.com
Date: 2023-09-07 10:21:31
LastEditors: lmio 2091319361@qq.com
Description: 2594. 修车的最少时间
'''

from math import floor, sqrt
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l , r = 1, ranks[0] * cars * cars
        def check(m: int) -> bool:
            return sum([floor(sqrt(m // x)) for x in ranks]) >= cars
        while l < r:
            m = (l + r) >> 1
            if check(m):
                r = m
            else:
                l = m + 1
        return l