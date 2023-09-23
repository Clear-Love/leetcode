'''
Author: lmio 2091319361@qq.com
Date: 2023-09-08 11:15:16
LastEditors: lmio 2091319361@qq.com
Description: 692. 前K个高频单词
'''

from collections import Counter
import heapq
from typing import List



class Solution(object):
    def topKFrequent(self, words: List[str], k: int):
        res = heapq.nsmallest(k, [(v, k) for k, v in Counter(words).items()], key=lambda a: (-a[0], a[1]))
        return [x[1] for x in res]