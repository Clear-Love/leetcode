'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 22:15:58
LastEditors: lmio 2091319361@qq.com
Description: 面试题 10.02. 变位词组
'''

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sort_s = ''.join(sorted(s))
            res[sort_s].append(s)
        return [val for val in res.values()]