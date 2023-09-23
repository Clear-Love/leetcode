'''
Author: lmio 2091319361@qq.com
Date: 2023-09-18 17:26:05
LastEditors: lmio 2091319361@qq.com
Description: 2226. 每个小孩最多能分到多少糖果
'''

from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        if sum([v for v in candies]) < k:
            return 0
        while l < r:
            mid = (l+r+1) >> 1
            if sum([v//mid for v in candies]) < k:
                r = mid-1
            else:
                l = mid
        return l