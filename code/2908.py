'''
Author: lmio 2091319361@qq.com
Date: 2023-10-23 13:00:10
LastEditors: lmio 2091319361@qq.com
Description: 2908. 元素和最小的山形三元组 I
'''

from math import inf
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_to_index = [nums[0]]
        right_to_index = [0]*n
        right_to_index[n-1] = nums[-1]
        for i in range(1, n):
            left_to_index.append(min(left_to_index[-1], nums[i]))
        for i in range(n-2, -1, -1):
            right_to_index[i] = min(right_to_index[i+1], nums[i])
        res = inf
        for i in range(1, n-1):
            l, r = left_to_index[i-1], right_to_index[i+1]
            if l < nums[i] > r:
                res = min(res, l+nums[i]+r)
        return res if res != inf else -1