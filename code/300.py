'''
Author: lmio 2091319361@qq.com
Date: 2023-08-21 21:27:16
LastEditors: lmio 2091319361@qq.com
Description: 300. 最长递增子序列
'''

import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            if num > stack[-1]:
                stack.append(num)
            else:
                idx = bisect.bisect_left(stack, num)
                stack[idx] = num
        return len(stack)