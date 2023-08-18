'''
Author: lmio 2091319361@qq.com
Date: 2023-08-16 20:12:43
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.16. 部分排序
'''

import bisect
from typing import List


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        if not array:
            return [-1, -1]
        n = len(array)
        left, right = 1, 0
        while left < n and array[left] > array[left-1]:
            left += 1
        if left == n:
            return [-1, -1]
        maxVal = max(array[:left])
        left = bisect.bisect_left(array[:left], array[left])
        for i in range(left, len(array)):
            v = array[i]
            maxVal = max(maxVal, v)
            if v >= maxVal:
                continue
            right = i
            if array[i] < array[left]:
                left = bisect.bisect_left(array[:left], array[i])
        return [left, right]