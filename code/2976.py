'''
Author: lmio 2091319361@qq.com
Date: 2024-05-24 19:27:17
LastEditors: lmio 2091319361@qq.com
Description: 2976. 转换字符串的最小成本 I
'''

from math import inf
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        N = 26
        dist = [[inf]*N for _ in range(N)]
        for i in range(len(original)):
            o, c = ord(original[i])-ord('a'), ord(changed[i])-ord('a')
            dist[o][c] = min(dist[o][c], cost[i])
        for i in range(N):
            dist[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        res = 0
        for i in range(len(source)):
            s, t = ord(source[i])-ord('a'), ord(target[i])-ord('a')
            c = dist[s][t]
            if c == inf:
                return -1
            res += c
        return res
