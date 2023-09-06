'''
Author: lmio 2091319361@qq.com
Date: 2023-09-05 08:09:29
LastEditors: lmio 2091319361@qq.com
Description: 2605. 从两个数字数组里生成最小数字
'''

from math import inf
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        v1 = min(nums1)
        nums1 = set(nums1)
        v2 = inf
        res = inf
        for v in nums2:
            if v in nums1:
                res = min(res, v)
            v2 = min(v2, v)
        if res != inf:
            return res
        return min(v1*10+v2, v2*10+v1)