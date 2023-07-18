'''
Author: lmio 2091319361@qq.com
Date: 2023-07-18 09:49:13
LastEditors: lmio 2091319361@qq.com
Description: 1851. 包含每个查询的最小区间
'''
import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        queries = sorted((x, i) for i, x in enumerate(queries))
        res = [-1] * len(queries)
        pq = []
        n = len(intervals)
        index = 0
        for v, i in queries:
            while index < n and intervals[index][0] <= v:
                l, r = intervals[index]
                index += 1
                heapq.heappush(pq, (r-l+1, r))
            while pq and pq[0][1] < v:
                heapq.heappop(pq)
            if pq:
                res[i] = pq[0][0]
        return res