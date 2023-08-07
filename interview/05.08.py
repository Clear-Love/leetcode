'''
Author: lmio 2091319361@qq.com
Date: 2023-08-07 12:46:27
LastEditors: lmio 2091319361@qq.com
Description: 面试题 05.08. 绘制直线
'''

import math
from typing import List


class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        m = 0xffffffff
        res = [0]*length
        w = w//32
        l, loffset = divmod(x1, 32)
        l += y*w
        r, roffset = divmod(x2, 32)
        r += y*w
        for i in range(l+1, r):
            res[i] = -1
        res[l] = res[l] | (m >> loffset)
        if l == r:
            res[r] = res[r] & (m << (31-roffset)) & m
        else:
            res[r] = res[r] | (m << (31-roffset)) & m
        res[l] = -((res[l]^m)+1) if res[l] & 0x80000000 == 0x80000000 else res[l]
        res[r] = -((res[r]^m)+1) if res[r] & 0x80000000 == 0x80000000 else res[r]
        return res