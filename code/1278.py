'''
Author: lmio 2091319361@qq.com
Date: 2023-10-24 19:35:07
LastEditors: lmio 2091319361@qq.com
Description: 1278. 分割回文串 III
'''

from functools import cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def min_modify(t: str) -> int:
            l, r = 0, len(t)-1
            diff = 0
            while l < r:
                if t[l] != t[r]:
                    diff += 1
                l += 1
                r -= 1
            return diff
        @cache
        def dfs(l: int, c: int) ->int:
            if c == 0:
                return min_modify(s[l:])
            res = n
            for r in range(l+1, n-c+1):
                res = min(res, min_modify(s[l:r])+dfs(r, c-1))
            return res
        return dfs(0, k-1)