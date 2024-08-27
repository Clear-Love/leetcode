'''
Author: lmio 2091319361@qq.com
Date: 2024-05-08 15:31:18
LastEditors: lmio 2091319361@qq.com
Description: 857. 雇佣 K 名工人的最低成本
'''

import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        # 按照单位质量的工资排序
        pairs = sorted(list(zip(quality, wage)), key=lambda x: x[1] / x[0])
        h = [-x[0] for x in pairs[:k]]
        heapq.heapify(h)
        s = -sum(h) #质量和
        res = s * pairs[k - 1][1]/pairs[k - 1][0]
        for q, w in pairs[k:]:
            if q < -h[0]:
                s += heapq.heapreplace(h, -q)
                s += q
                res = min(res, s * w/q)
        return res