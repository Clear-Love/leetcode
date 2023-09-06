'''
Author: lmio 2091319361@qq.com
Date: 2023-09-02 15:16:52
LastEditors: lmio 2091319361@qq.com
Description: 647. 回文子串
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        def f(l: int, r: int) -> int:
            cnt = 0
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                cnt += 1
                l -= 1
                r += 1
            return cnt
        for i in range(len(s)):
            res += f(i, i) + f(i, i+1)
        return res