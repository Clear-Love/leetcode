'''
Author: lmio 2091319361@qq.com
Date: 2023-08-13 10:30:35
LastEditors: lmio 2091319361@qq.com
Description: 6939. 数组中的最大数对和
'''

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def maxVal(n: int):
            res = 0
            while n > 0:
                n, v = divmod(n, 10)
                res = max(res, v)
            return res
        m = defaultdict(list)
        for v in nums:
            x = maxVal(v)
            arr = m[x]
            if len(arr) == 2:
                heapq.heappush(arr, v)
                heapq.heappop(arr)
            else:
                heapq.heappush(arr, v)
            m[x] = arr
        res = -1
        for arr in m.values():
            if len(arr) != 2:
                continue
            res = max(res, sum(arr))
        return res