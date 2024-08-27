'''
Author: lmio 2091319361@qq.com
Date: 2024-03-30 23:20:38
LastEditors: lmio 2091319361@qq.com
Description: 100271. 或值至少为 K 的最短子数组 II
'''

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preOr = []
        s = 0
        for num in nums:
            s |= num
            preOr.append(s)
        for i in range(n):
            v = preOr[]