'''
Author: lmio 2091319361@qq.com
Date: 2023-09-08 10:56:19
LastEditors: lmio 2091319361@qq.com
Description: 347. 前 K 个高频元素
'''

from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = Counter(nums)
        res = []
        for v in cnts.keys():
            if len(res) < k:
                heapq.heappush(res, (cnts[v], v))
            elif cnts[v] > res[0][0]:
                heapq.heapreplace(res, (cnts[v], v))
        return [v[1] for v in res]