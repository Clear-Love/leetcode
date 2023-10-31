'''
Author: lmio 2091319361@qq.com
Date: 2023-10-24 15:16:17
LastEditors: lmio 2091319361@qq.com
Description: 1155. 掷骰子等于目标和的方法数
'''
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(c: int, t: int) ->int:
            if c == 0:
                return 1
            l, r = max(1, t-k*c), min(k, t-c)
            cnt = 0
            for i in range(l, r+1):
                cnt += dfs(c-1, t-i)
            return cnt%MOD
        if n*k < target:
            return 0
        return dfs(n-1, target)