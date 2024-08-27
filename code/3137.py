'''
Author: lmio 2091319361@qq.com
Date: 2024-05-06 16:06:39
LastEditors: lmio 2091319361@qq.com
Description: 3137. K 周期字符串需要的最少操作次数
'''

from typing import Counter


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        c = n//k
        cnts = Counter()
        for i in range(0, n-k+1, k):
            cnts[word[i:i+k]] += 1
        return min(c-v for v in cnts.values())