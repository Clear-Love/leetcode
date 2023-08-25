'''
Author: lmio 2091319361@qq.com
Date: 2023-07-04 20:57:26
LastEditors: lmio 2091319361@qq.com
Description: 76. 最小覆盖子串
'''

from collections import Counter



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        res = [0, len(s)]
        m = set(t)
        tc = Counter(t)
        sc = Counter()
        def contain(cnts: Counter):
            for ch in tc:
                if cnts[ch] < tc[ch]:
                    return False
            return True
        for right, ch in enumerate(s):
            if ch not in m:
                continue
            sc[ch]+=1
            if not contain(sc):
                continue
            while left <= right:
                if right - left < res[1] - res[0]:
                    res[0] = left
                    res[1] = right
                if s[left] in m:
                    sc[s[left]] -= 1
                    if sc[s[left]] < tc[s[left]]:
                        left += 1
                        break
                left+=1
        return s[res[0]: res[1]+1] if res[1] != len(s) else ''