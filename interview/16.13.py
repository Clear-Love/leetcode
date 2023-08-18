'''
Author: lmio 2091319361@qq.com
Date: 2023-08-14 18:14:18
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.13. 平分正方形
'''

from typing import List


class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        if square1[0] > square2[0]:
            return self.cutSquares(square2, square1)
        l1, l2 = square1[2], square2[2]
        x1, y1 = square1[0] + l1/2, square1[1] + l1/2
        x2, y2 = square2[0] + l2/2, square2[1] + l2/2
        if x1 == x2 or (x1, y1) == (x2, y2):
            return [x1, min(square1[1], square2[1]), x2, max(square2[1]+l2, square1[1]+l1)]
        k = (y1-y2)/(x1-x2)
        b = y1 - k*x1
        if k > 1:
            y1 = min(square1[1], square2[1])
            x1 = (y1-b)/k
            y2 = max(square1[1] + l1, square2[1] + l2)
            x2 = (y2-b)/k
        elif k < -1:
            y1 = max(square1[1] + l1, square2[1] + l2)
            x1 = (y1-b)/k
            y2 = min(square1[1], square2[1])
            x2 = (y2-b)/k
        else:
            x1 = square1[0]
            y1 = k*x1 + b
            x2 = max(square1[0] + l1, square2[0] + l2)
            y2 = k*x2 + b
        return [x1, y1, x2, y2]