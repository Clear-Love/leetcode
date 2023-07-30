'''
Author: lmio 2091319361@qq.com
Date: 2023-07-30 16:11:44
LastEditors: lmio 2091319361@qq.com
Description: 2542. 最大子序列的分数
'''
import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        hq = []
        s = 0
        for v in arr[:k]:
            heapq.heappush(hq, v[0])
            s += v[0]
        res = arr[k-1][1]*s
        for x, y in arr[k:]:
            if x > hq[0]:
                s = s - heapq.heapreplace(hq, x) + x
                res = max(res, y*s)
        return res