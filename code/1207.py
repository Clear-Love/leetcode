'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 22:05:03
LastEditors: lmio 2091319361@qq.com
Description: 1207. 独一无二的出现次数
'''

from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnts = Counter(arr)
        vals = set()
        for cnt in cnts.values():
            if cnt not in vals:
                vals.add(cnt)
            else:
                return False
        return True