'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 21:52:46
LastEditors: lmio 2091319361@qq.com
Description: 1732. 找到最高海拔
'''

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        res = 0
        for v in gain:
            curr += v
            res = max(res, curr)
        return res