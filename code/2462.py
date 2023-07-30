'''
Author: lmio 2091319361@qq.com
Date: 2023-07-30 17:51:20
LastEditors: lmio 2091319361@qq.com
Description: 2462. 雇佣 K 位工人的总代价
'''
import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res, n = 0, len(costs)
        if candidates * 2 < n:
            pre = costs[:candidates]
            heapq.heapify(pre)
            suf = costs[-candidates:]
            heapq.heapify(suf) 
            left, right = candidates, n - 1 - candidates
            while k and left <= right:
                if pre[0] <= suf[0]:
                    res += heapq.heapreplace(pre, costs[left])
                    left += 1
                else:
                    res += heapq.heapreplace(suf, costs[right])
                    right -= 1
                k -= 1
            costs = pre + suf
        costs.sort()
        return res + sum(costs[:k])