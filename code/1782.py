'''
Author: lmio 2091319361@qq.com
Date: 2023-08-23 21:25:52
LastEditors: lmio 2091319361@qq.com
Description: 1782. 统计点对的数目
'''

import bisect
from collections import defaultdict
from itertools import accumulate
from typing import Counter, List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        cnts = [0] * (n + 1)
        res = [0] * len(queries)
        shared = Counter(tuple(sorted(edge)) for edge in edges)
        for u, v in edges:
            cnts[u] += 1
            cnts[v] += 1
        sorted_cnt = sorted(cnts)
        for k, q in enumerate(queries):
            i, j = 1, n 
            while i < j:
                if q < sorted_cnt[i] + sorted_cnt[j]:
                    res[k] += j - i
                    j -= 1
                else:
                    i += 1
            for (i, j), cnt in shared.items():
                if q < cnts[i] + cnts[j] <= q + cnt:
                    res[k] -= 1;
        return res