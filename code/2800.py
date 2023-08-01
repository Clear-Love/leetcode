'''
Author: lmio 2091319361@qq.com
Date: 2023-08-01 08:38:50
LastEditors: lmio 2091319361@qq.com
Description: 2800. 包含三个字符串的最短字符串
'''
from itertools import permutations


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(s: str, t: str) -> str:
            # 先特判完全包含的情况
            if t in s: return s
            if s in t: return t
            for i in range(len(s)):
                if t.startswith(s[i:]):
                    return s + t[len(s)-i:]
            return s + t
        res = ""
        for a, b, c in permutations((a, b, c)):
            s = merge(merge(a, b), c)
            if res == "" or len(s) < len(res) or (len(s) == len(res) and s < res):
                res = s
        return res