'''
Author: lmio 2091319361@qq.com
Date: 2023-09-20 21:53:08
LastEditors: lmio 2091319361@qq.com
Description: 2513. 最小化两个数组中的最大值
'''

from bisect import bisect_left
import math
class Solution:
    def minimizeSet(self, d1: int, d2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lcm = math.lcm(d1, d2)
        return bisect_left(range((uniqueCnt1 + uniqueCnt2) * 2 - 1), True,\
                           key=lambda v: (v - v // d1 >= uniqueCnt1) and\
                           (v - v // d2 >= uniqueCnt2) and\
                           (v - v // lcm >= uniqueCnt1 + uniqueCnt2))