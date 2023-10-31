'''
Author: lmio 2091319361@qq.com
Date: 2023-10-30 16:41:36
LastEditors: lmio 2091319361@qq.com
Description: 275. H 指数 II
'''

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, min(len(citations), citations[-1])
        while left < right:
            mid = (left+right+1) >> 1
            if citations[-mid] >= mid:
                left = mid
            else:
                right = mid-1
        return left