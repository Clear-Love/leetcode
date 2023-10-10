'''
Author: lmio 2091319361@qq.com
Date: 2023-10-01 10:30:22
LastEditors: lmio 2091319361@qq.com
Description: 100088. 有序三元组中的最大值 I
'''

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        s = 0
        res = 0
        n = len(nums)
        def dfs(i: int, k: int):
            nonlocal s, res
            if k == 3:
                res = max(res, s)
                return
            for j in range(i, n):
                if k == 0:
                    s += nums[j]
                elif k == 1:
                    s -= nums[j]
                else:
                    s *= nums[j]
                dfs(j+1, k+1)
                if k == 0:
                    s -= nums[j]
                elif k == 1:
                    s += nums[j]
                else:
                    s //= nums[j]
        dfs(0, 0)
        return res