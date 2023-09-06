'''
Author: lmio 2091319361@qq.com
Date: 2023-09-05 09:16:34
LastEditors: lmio 2091319361@qq.com
Description: 1936. 新增的最少台阶数
'''

from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        cur = 0
        res = 0
        for h in rungs:
            if h - cur > dist:
                res += (h-cur-1)//dist
            cur = h
        return res