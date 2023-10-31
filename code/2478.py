'''
Author: lmio 2091319361@qq.com
Date: 2023-10-24 20:46:58
LastEditors: lmio 2091319361@qq.com
Description: 2478. 完美分割的方案数
'''

from functools import cache


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9+7
        prime_index = [i for i in range(len(s)) if s[i] in '2357']
        n, m = len(prime_index), len(s)
        if len(prime_index) < k or prime_index[0] != 0 or prime_index[-1] == m-1:
            return 0
        @cache
        def dfs(i: int, c: int) ->int:
            l = prime_index[i]
            if c == 0:
                return 1 if m-l >= minLength else 0
            cnt = 0
            for j in range(i+1, n-c+1):
                r = prime_index[j]
                if m-r < c*minLength:
                    break
                if r - l < minLength or prime_index[j-1] == r-1:
                    continue
                cnt += dfs(j, c-1)
            return cnt%MOD
        return dfs(0, k-1)