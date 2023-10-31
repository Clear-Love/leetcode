'''
Author: lmio 2091319361@qq.com
Date: 2023-10-20 12:47:11
LastEditors: lmio 2091319361@qq.com
Description: 2901. 最长相邻不相等子序列 II
'''

from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def isOK(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return False
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        dp = [0]*n
        fr = [i for i in range(n)]
        max_idx = 0
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if dp[j] > dp[i] and groups[i] != groups[j] and isOK(words[i], words[j]):
                    dp[i] = dp[j]
                    fr[i] = j
            dp[i] += 1
            if dp[i] > dp[max_idx]:
                max_idx = i
        res = []
        i = max_idx
        while fr[i] != i:
            res.append(words[i])
            i = fr[i]
        res.append(words[i])
        return res