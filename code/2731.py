'''
Author: lmio 2091319361@qq.com
Date: 2023-10-13 16:50:42
LastEditors: lmio 2091319361@qq.com
Description: 2731. 移动机器人
'''
from typing import List


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        rotd = {}
        MOD = 10**9+7
        n = len(nums)
        for i, ch in enumerate(s):
            rotd[i] = 1 if ch == 'R' else -1
        for i in range(n):
            nums[i] += d*rotd[i]
        nums.sort()
        res = 0
        s = 0
        for i in range(1, n):
            s = (nums[i]-nums[i-1])*i+s
            res += s
        return res%MOD