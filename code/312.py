'''
Author: lmio 2091319361@qq.com
Date: 2023-10-20 18:02:01
LastEditors: lmio 2091319361@qq.com
Description: 312. 戳气球
'''

from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        @cache
        def dfs(l: int, r: int):
            if l >= r:
                return 0
            mx = 0
            for i in range(l+1, r):
                mx = max(mx, nums[l]*nums[i]*nums[r] + dfs(l, i) + dfs(i, r))
            return mx
        return dfs(0, len(nums)-1)