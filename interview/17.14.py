'''
Author: lmio 2091319361@qq.com
Date: 2023-08-24 20:38:05
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.14. 最小K个数
'''

import heapq
from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        q = []
        for i in range(len(arr)):
            heapq.heappush(q, arr[i])
        return [heapq.heappop(q) for _ in range(k)]