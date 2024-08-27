'''
Author: lmio 2091319361@qq.com
Date: 2024-03-22 23:37:57
LastEditors: lmio 2091319361@qq.com
Description: 2617. 网格图中最少访问的格子数
'''

import heapq
from typing import List


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        