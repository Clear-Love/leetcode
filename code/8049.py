'''
Author: lmio 2091319361@qq.com
Date: 2023-09-10 10:50:11
LastEditors: lmio 2091319361@qq.com
Description: 8049. 判断能否在给定时间到达单元格
'''

from collections import deque
from msvcrt import setmode


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx, dy = abs(sx-fx), abs(sy-fy)
        step = abs(dx - dy) + min(dx, dy)
        if step == 0 and t == 1:
            return False
        return step <= t