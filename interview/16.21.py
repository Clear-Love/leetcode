'''
Author: lmio 2091319361@qq.com
Date: 2023-08-17 21:22:24
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.21. 交换和
'''

from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        s1, s2 = sum(array1), sum(array2)
        gap = (s1-s2) >> 1
        if gap*2 != s1 - s2:
            return []
        m = set(array2)
        for v in array1:
            if v - gap in m:
                return [v, v-gap]
        return []