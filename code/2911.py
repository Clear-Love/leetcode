'''
Author: lmio 2091319361@qq.com
Date: 2023-10-23 18:58:10
LastEditors: lmio 2091319361@qq.com
Description: 2911. 得到 K 个半回文串的最少修改次数
'''

from functools import cache

MX = 201
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i * 2, MX, i):
        divisors[j].append(i)

@cache
def get_modify(s: str) ->int:
    n = len(s)
    res = n
    for d in divisors[n]:
        diff = 0
        for l in range(d):
            r = n-d+l
            while l < r:
                if s[l] != s[r]:
                    diff += 1
                l += d
                r -= d
        res = min(res, diff)
    return res

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def dfs(r:int, c: int) ->int:
            if c == 0:
                return get_modify(s[:r+1])
            return min(get_modify(s[l:r+1]) + dfs(l-1, c-1) for l in range(c*2, r))
        return dfs(n-1, k-1)

print(get_modify('abcc'))