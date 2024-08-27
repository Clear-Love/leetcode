'''
Author: lmio 2091319361@qq.com
Date: 2024-03-17 10:44:32
LastEditors: lmio 2091319361@qq.com
Description: 100255. 成为 K 特殊字符串需要删除的最少字符数
'''

from math import inf
from typing import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnts = sorted(Counter(word).values())
        res = inf
        repr()
        for i, c in enumerate(cnts):
            res = min(res, sum(cnts[x] for x in range(i) if cnts[x] < c)+sum(cnts[x]-k-c for x in range(i, len(cnts)) if cnts[x] > c+k))
        return res