'''
Author: lmio 2091319361@qq.com
Date: 2023-10-20 12:23:56
LastEditors: lmio 2091319361@qq.com
Description: 2900. 最长相邻不相等子序列 I
'''

from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        want = groups[0]
        res = []
        for i in range(n):
            if groups[i] == want:
                res.append(words[i])
                want ^= 1
        return res