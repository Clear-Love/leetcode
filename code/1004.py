'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 21:01:24
LastEditors: lmio 2091319361@qq.com
Description: 1004. 最大连续1的个数 III
'''

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        q = []
        res = 0
        while right < len(nums):
            if nums[right] == 0:
                q.append(right)
            if len(q) > k:
                left = q[0] + 1
                q = q[1:]
            res = max(res, right - left + 1)
            right += 1
        return res