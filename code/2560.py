'''
Author: lmio 2091319361@qq.com
Date: 2023-09-19 11:58:20
LastEditors: lmio 2091319361@qq.com
Description: 2560. 打家劫舍 IV
'''

from bisect import bisect_left
from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def solve(mx: int) -> int:
            cnt = i = 0
            while i < len(nums):
                if nums[i] > mx:
                    i += 1
                else:
                    cnt += 1
                    i += 2
            return cnt
        return bisect_left(range(max(nums)), k, key=solve)