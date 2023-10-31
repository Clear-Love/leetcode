'''
Author: lmio 2091319361@qq.com
Date: 2023-10-26 10:24:51
LastEditors: lmio 2091319361@qq.com
Description: 503. 下一个更大元素 II
'''

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums
        res = [-1]*n
        stack = []
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] < v:
                res[stack.pop()%n] = v
            stack.append(i)
        return res