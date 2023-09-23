'''
Author: lmio 2091319361@qq.com
Date: 2023-09-17 19:41:44
LastEditors: lmio 2091319361@qq.com
Description: 1222. 可以攻击国王的皇后
'''

from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        x, y = king
        anti = x+y
        forw = x-y
        res = [[] for _ in range(8)]
        for i, j in queens:
            if i == x:
                if j < y and (not res[3] or j > res[3][1]):
                    res[3] = [i, j]
                if j > y and (not res[4] or j < res[4][1]):
                    res[4] = [i, j]
            if j == y:
                if i < x and (not res[1] or i > res[1][0]):
                    res[1] = [i, j]
                if i > x and (not res[6] or i < res[6][0]):
                    res[6] = [i, j]
            if i-j == forw:
                if j < y and (not res[5] or j > res[5][1]):
                    res[5] = [i, j]
                if j > y and (not res[2] or j < res[2][1]):
                    res[2] = [i, j]
            if i+j == anti:
                if j < y and (not res[0] or j > res[0][1]):
                    res[0] = [i, j]
                if j > y and (not res[7] or j < res[7][1]):
                    res[7] = [i, j]
        return [v for v in res if v]