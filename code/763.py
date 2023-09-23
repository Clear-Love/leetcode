'''
Author: lmio 2091319361@qq.com
Date: 2023-09-09 21:18:01
LastEditors: lmio 2091319361@qq.com
Description: 763. 划分字母区间
'''

from collections import OrderedDict, defaultdict
import enum
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = dict()
        for idx, c in enumerate(s):
            d[c] = idx
        res = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, d[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res