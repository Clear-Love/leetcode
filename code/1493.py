'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 21:44:16
LastEditors: lmio 2091319361@qq.com
Description: 1493. 删掉一个元素以后全为 1 的最长子数组
'''

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroIndex = []
        left, right = 0, 0
        res = 0
        while right < len(nums):
            if nums[right] == 0:
                zeroIndex.append(right)
            if len(zeroIndex) > 1:
                left = zeroIndex.pop(0)+1
            res = max(res, right - left)
            right += 1
        return res