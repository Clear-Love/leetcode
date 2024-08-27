'''
Author: lmio 2091319361@qq.com
Date: 2024-03-18 16:13:27
LastEditors: lmio 2091319361@qq.com
Description: 871. 最低加油次数
'''

import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        stations.append([target, 0])
        q = []
        total = startFuel
        cnt = 0
        for pos, fuel in stations:
            while q and total < pos:
                total += -heapq.heappop(q)
                cnt += 1
            if total < pos:
                return -1
            if total >= target:
                return cnt
            heapq.heappush(q, -fuel)
        return -1