'''
Author: lmio 2091319361@qq.com
Date: 2023-08-01 22:19:03
LastEditors: lmio 2091319361@qq.com
Description: 600. 不含连续1的非负整数
'''

from functools import cache


class Solution:
    def findIntegers(self, n: int) -> int:
        n = bin(n)
        n = n[2:]
        @cache
        def f(i: int, pre: int, isLimit: bool, isNum: bool) -> int:
            res = 0
            if i == len(n):
                return int(isNum)
            if not isNum:
                res += f(i+1, 0, False, False)
            low = 0 if isNum else 1
            if isLimit:
                up = 1 if n[i] == '1' else 0
            else:
                up = 1
            for d in range(low, up+1):
                # 非连续的1
                if pre & d != 1:
                    res += f(i+1, d, isLimit and d == up, True)
            return res
        return f(0, 0, True, False)+1

s = Solution()
print(s.findIntegers(2))