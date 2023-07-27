'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 21:59:05
LastEditors: lmio 2091319361@qq.com
Description: 2215. 找出两数组的不同
'''
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[] for _ in range(2)]
        m1, m2 = set(nums1), set(nums2)
        for v in m1:
            if v not in m2:
                res[0].append(v)
        for v in m2:
            if v not in m1:
                res[1].append(v)
        return res