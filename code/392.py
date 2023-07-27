'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 20:25:46
LastEditors: lmio 2091319361@qq.com
Description: 392. 判断子序列
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n > m:
            return False
        i, j = 0, 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n