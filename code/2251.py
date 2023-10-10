'''
Author: lmio 2091319361@qq.com
Date: 2023-09-28 16:38:50
LastEditors: lmio 2091319361@qq.com
Description: 2251. 花期内花的数目
'''

from collections import Counter, defaultdict
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        diff = defaultdict(int)
        for start, end in flowers:
            diff[start-1] += 1
            diff[end] -= 1
        n = len(people)
        times = sorted(diff.keys())
        res = [0]*n
        s = 0
        index = 0
        for day, i in sorted([(v, i) for i, v in enumerate(people)]):
            while index < len(times) and times[index] < day:
                s += diff[times[index]]
                index += 1
            res[i] = s
        return res