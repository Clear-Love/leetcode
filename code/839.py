'''
Author: lmio 2091319361@qq.com
Date: 2023-10-17 21:17:14
LastEditors: lmio 2091319361@qq.com
Description: 839. 相似字符串组
'''

from itertools import combinations
from typing import List

from utils.unionFind import unionFind


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = unionFind()
        def is_similar(x: str, y: str) -> bool:
            diff = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    diff += 1
            return diff <= 2
        for x, y in combinations(strs, 2):
            if is_similar(x, y):
                uf.union(x, y)
        com = set(uf.find(s) for s in strs)
        return len(com)