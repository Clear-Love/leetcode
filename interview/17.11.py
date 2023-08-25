'''
Author: lmio 2091319361@qq.com
Date: 2023-08-22 16:46:50
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.11. 单词距离
'''

import bisect
from collections import defaultdict
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        pos = defaultdict(list)
        for i, word in enumerate(words):
            pos[word].append(i)
        l1, l2 = pos[word1], pos[word2]
        res = float('inf')
        j = 0
        for v in l1:
            while j < len(l2)-1 and l2[j] < v:
                j += 1
            pre = max(0, j-1)
            res = min(res, abs(v-l2[pre]), abs(v-l2[j]))
        return res