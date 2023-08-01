'''
Author: lmio 2091319361@qq.com
Date: 2023-08-01 22:53:13
LastEditors: lmio 2091319361@qq.com
Description: 902. 最大为 N 的数字组合
'''

from functools import cache
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = str(n)
        digits = set(int(x) for x in digits)
        @cache
        def f(i: int, isLimit: bool, isNum: bool):
            res = 0
            if i == len(n):
                return int(isNum)
            if not isNum:
                res += f(i+1, False, False)
            low = 0 if isNum else 1
            up = int(n[i]) if isLimit else 9
            for d in range(low, up+1):
                if d not in digits:
                    continue
                res += f(i+1, isLimit and d == up, True)
            return res
        return f(0, True, False)