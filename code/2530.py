'''
Author: lmio 2091319361@qq.com
Date: 2023-10-18 10:58:53
LastEditors: lmio 2091319361@qq.com
Description: 2530. 执行 K 次操作后的最大分数
'''

import heapq
import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = heapq.nlargest(min(k, n), nums)
        q = [-v for v in q]
        heapq.heapify(q)
        res = 0
        for _ in range(k):
            score = -heapq.heappop(q)
            res += score
            heapq.heappush(q, -math.ceil(score/3))
        return res