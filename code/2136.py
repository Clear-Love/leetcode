'''
Author: lmio 2091319361@qq.com
Date: 2023-09-30 16:50:41
LastEditors: lmio 2091319361@qq.com
Description: 2136. 全部开花的最早一天
'''

from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        growTime = sorted([(v, i) for i, v in enumerate(growTime)], reverse=True)
        res = 0
        t = 0
        for v, i in growTime:
            t += plantTime[i]
            res = max(res, t+v)
        return res