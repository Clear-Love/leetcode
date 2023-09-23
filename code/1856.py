'''
Author: lmio 2091319361@qq.com
Date: 2023-09-07 15:04:25
LastEditors: lmio 2091319361@qq.com
Description: 1856. 子数组最小乘积的最大值
'''

from itertools import accumulate
from tracemalloc import start
from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        nums.append(1)
        MOD = 10**9+7
        s = [0]*(len(nums)+1)
        stack = [-1]
        res = 0
        for i,v in enumerate(nums):
            s[i+1] = s[i]+v
            while stack and nums[stack[-1]] > v:
                idx = stack.pop()
                left = stack[-1]
                res = max(res,(s[i]-s[left+1])*nums[idx])
            stack.append(i)
        return res%MOD