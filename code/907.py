'''
Author: lmio 2091319361@qq.com
Date: 2023-09-05 09:27:25
LastEditors: lmio 2091319361@qq.com
Description: 907. 子数组的最小值之和
'''

from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        arr.append(-1)
        MOD = 10**9+7
        stack = [(-1, -1)]
        for i, v in enumerate(arr):
            while len(stack) > 1 and stack[-1][0] > v:
                e, j = stack.pop()
                res += (e*(j-stack[-1][1])*(i-j))%MOD
            stack.append((v, i))
        return res%MOD