'''
Author: lmio 2091319361@qq.com
Date: 2023-08-01 23:53:35
LastEditors: lmio 2091319361@qq.com
Description: 1012. 至少有 1 位重复的数字
'''

from functools import cache


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        n = str(n)
        @cache
        def f(i: int, nums: int, isLimit: bool, isNum: bool, valid: bool):
            res = 0
            if i == len(n):
                return int(valid)
            if not isNum:
                res += f(i+1,nums, False, False, False)
            low = 0 if isNum else 1
            up = int(n[i]) if isLimit else 9
            for d in range(low, up+1):
                if (nums >> d) & 1 == 1:
                    res += f(i+1, nums, isLimit and d == up, True, True)
                else:
                    nums = nums | (1 << d)
                    res += f(i+1, nums, isLimit and d == up, True, valid)
                    nums = nums & ~(1 << d)
            return res
        return f(0, 0, True, False, False)