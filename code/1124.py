'''
Author: lmio 2091319361@qq.com
Date: 2023-10-27 14:12:16
LastEditors: lmio 2091319361@qq.com
Description: 1124. 表现良好的最长时间段
'''

from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        stack = [0]
        preSum = [0]*(n+1)
        for i, h in enumerate(hours, 1):
            preSum[i] = preSum[i-1] + (1 if h > 8 else -1)
            if preSum[i] < preSum[stack[-1]]:
                stack.append(i)
        res = 0
        for j in range(n, 0, -1):
            s = preSum[j]
            while stack and preSum[stack[-1]] < s:
                res = max(res, j-stack.pop())
        return res