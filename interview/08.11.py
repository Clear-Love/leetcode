'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 15:16:35
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.11. 硬币
'''

from functools import cache


class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [25, 10, 5, 1]
        MOD = 1000000007
        @cache
        def dfs(i: int, s):
            cnt = 0
            if s == n:
               return 1
            for j in range(i, 4):
                if s + coins[j] > n:
                    continue
                cnt += dfs(j, s+coins[j])
            return cnt
        return dfs(0, 0) % MOD