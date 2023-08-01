'''
Author: lmio 2091319361@qq.com
Date: 2023-07-31 20:37:28
LastEditors: lmio 2091319361@qq.com
Description: 739. 每日温度
'''

from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = deque()
        stack.append(0)
        res = [0]*n
        for i in range(1, n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res