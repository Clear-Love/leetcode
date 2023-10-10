'''
Author: lmio 2091319361@qq.com
Date: 2023-10-06 23:30:14
LastEditors: lmio 2091319361@qq.com
Description: 
'''

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0]*n
        for _, j in edges:
            degree[j] += 1
        return [i for i in range(n) if not degree[i]]