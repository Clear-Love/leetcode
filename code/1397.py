from functools import cache
from string import ascii_lowercase


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        next = [0]
        MOD = 10**9 + 7
        k = 0
        # 求next数组
        for i in range(1, len(evil)):
            while k and evil[k] != evil[i]:
                k = next[k-1]
            if evil[k] == evil[i]:
                k += 1
            next.append(k)
        @cache
        def fn(i, k, isLow, isUp):
            if k == len(evil):
                return 0
            if i == n: return 1
            low = ascii_lowercase.index(s1[i]) if isLow else 0
            up = ascii_lowercase.index(s2[i]) if isUp else 25
            ans = 0
            for x in range(low, up+1):
                # 通过next数组计算evil匹配长度
                nk = k
                while nk and evil[nk] != ascii_lowercase[x]:
                    nk = next[nk-1]
                if evil[nk] == ascii_lowercase[x]:
                    nk += 1
                ans += fn(i+1, nk, isLow and x == low, isUp and x == up) % MOD
            return ans % MOD
        return fn(0, 0, True, True) % MOD