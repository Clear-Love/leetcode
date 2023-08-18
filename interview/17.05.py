'''
Author: lmio 2091319361@qq.com
Date: 2023-08-18 21:11:06
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.05. 字母与数字
'''

from collections import defaultdict
from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        numCnt, letterCnt = 0, 0
        pre = [0]
        gap = {}
        gap[0] = -1
        for i, v in enumerate(array):
            if v.isdigit():
                numCnt += 1
            else:
                letterCnt += 1
            pre.append(numCnt-letterCnt)
            gap[numCnt-letterCnt] = i
        left, right = 0, gap[0]
        size = right - left
        for i, v in enumerate(pre):
            j = gap[v]
            if j - i > size:
                left, right = i, j
                size = j - i
        return array[left:right+1]