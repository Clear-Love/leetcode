'''
Author: lmio 2091319361@qq.com
Date: 2023-08-01 19:28:42
LastEditors: lmio 2091319361@qq.com
Description: 233. 数字 1 的个数
'''

from functools import cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        n = str(n)
        @cache
        def f(i: int, isLimit: bool, isNum: bool, cnt: int) -> int:
            res = 0
            if i == len(n):
                return cnt
            if not isNum:
                res += f(i+1, False, False, 0)
            low = 0 if isNum else 1
            up = int(n[i]) if isLimit else 9
            for d in range(low, up+1):
                if d == 1:
                    res += f(i+1, isLimit and d == up, True, cnt+1)
                else:
                    res += f(i+1, isLimit and d == up, True, cnt)
            return res
        return f(0, True, False, 0)