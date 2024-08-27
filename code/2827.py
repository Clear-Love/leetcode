'''
Author: lmio 2091319361@qq.com
Date: 2024-05-30 20:00:44
LastEditors: lmio 2091319361@qq.com
Description: 2827. 范围中美丽整数的数目
'''

from functools import cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def calc(num: int) -> int:
            s = str(num)
            @cache
            def dfs(i: int, val: int, diff: int, isLimit: bool, isNum: bool) -> int:
                if i == len(s):
                    return int(diff == 0 and isNum and val == 0)
                res = 0
                up = int(s[i]) if isLimit else 9
                down = 0 if isNum else 1
                if not isNum:
                    # 忽略这一位
                    res += dfs(i+1, val, diff, False, isNum)
                for x in range(down, up+1):
                    if x&1 == 0:
                        res += dfs(i+1, (val*10+x)%k, diff+1, isLimit and x == up, True)
                    else:
                        res += dfs(i+1, (val*10+x)%k, diff-1, isLimit and x == up, True)
                return res
            ans = dfs(0, 0, 0, True, False)
            del dfs
            return ans
        return calc(high) - calc(low-1)