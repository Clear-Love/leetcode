'''
Author: lmio 2091319361@qq.com
Date: 2023-10-24 17:08:52
LastEditors: lmio 2091319361@qq.com
Description: 813. 最大平均值和的分组
'''

from functools import cache
from itertools import accumulate
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        preSum = list(accumulate(nums, initial=0))
        @cache
        def dfs(l: int, c: int) ->int:
            if l == n:
                return 0
            if not c:
                return (preSum[n] - preSum[l])/(n-l)
            res = 0
            for r in range(l+1, n+1):
                res = max(res, (preSum[r] - preSum[l])/(r-l)+dfs(r, c-1))
            return res
        return dfs(0, k-1)