'''
Author: lmio 2091319361@qq.com
Date: 2023-07-22 22:31:15
LastEditors: lmio 2091319361@qq.com
Description: 135. 分发糖果
'''
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        candynum = length
        left = [0] * length
        right = [0] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
        for i in range(length):
            candynum += max(left[i], right[i])
        return candynum