'''
Author: lmio 2091319361@qq.com
Date: 2023-07-15 15:00:39
LastEditors: lmio 2091319361@qq.com
Description: 
'''
import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        ind = list(range(n))
        # 按照资本排序
        ind.sort(key=lambda x: capital[x])
        stack = []
        j = 0
        for _ in range(k):
            # 将符合条件的加入备选队列
            while j < n and capital[ind[j]] <= w:
                heapq.heappush(stack, -profits[ind[j]])
                j += 1
            if not stack:
                return w
            w -= heapq.heappop(stack)
        return w