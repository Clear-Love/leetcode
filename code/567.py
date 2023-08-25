'''
Author: lmio 2091319361@qq.com
Date: 2023-08-25 22:15:50
LastEditors: lmio 2091319361@qq.com
Description: 567. 字符串的排列
'''

from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = set(s1)
        k = len(s1)
        if len(s2) < k:
            return False
        cnts1 = Counter(s1)
        cnts = defaultdict(int)
        def contain() -> bool:
            for ch in m:
                if cnts[ch] != cnts1[ch]:
                    return False
            return True
        left = 0
        for i in range(k):
            cnts[s2[i]] += 1
        if contain():
            return True
        for right in range(k, len(s2)):
            cnts[s2[left]] -= 1
            cnts[s2[right]] += 1
            left += 1
            if s2[right] in m and contain():
                return True
        return False

s = Solution()
print(s.checkInclusion("ab", "a"))