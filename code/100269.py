'''
Author: lmio 2091319361@qq.com
Date: 2024-05-12 10:30:51
LastEditors: lmio 2091319361@qq.com
Description: 100296. 两个字符串的排列差
'''

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        m = {}
        res = 0
        for i, c in enumerate(s):
            m[c] = i
        for i, c in enumerate(t):
            res += abs(m[c]-i)
        return res