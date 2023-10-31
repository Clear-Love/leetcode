'''
Author: lmio 2091319361@qq.com
Date: 2023-10-26 10:15:11
LastEditors: lmio 2091319361@qq.com
Description: 496. 下一个更大元素 I
'''

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                m[stack.pop()] = num
            stack.append(num)
        res = []
        for num in nums1:
            if num in m:
                res.append(m[num])
            else:
                res.append(-1)
        return res