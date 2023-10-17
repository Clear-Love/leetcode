'''
Author: lmio 2091319361@qq.com
Date: 2023-10-15 15:46:09
LastEditors: lmio 2091319361@qq.com
Description: 997. 找到小镇的法官
'''

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        entry = [0]*(n+1)
        out = [0]*(n+1)
        for u, v in trust:
            entry[v] += 1
            out[u] += 1
        for i in range(1, n+1):
            if entry[i] == n-1 and out[i] == 0:
                return i
        return -1