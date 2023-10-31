'''
Author: lmio 2091319361@qq.com
Date: 2023-10-30 17:05:53
LastEditors: lmio 2091319361@qq.com
Description: 84. 柱状图中最大的矩形
'''

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1] 
        res = 0
        heights = heights + [0]
        for i in range(len(heights)):
            while stack[-1]!=-1 and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res ,(i-stack[-1]-1)*heights[tmp])
            stack.append(i)
        return res