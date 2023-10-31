'''
Author: lmio 2091319361@qq.com
Date: 2023-10-26 10:32:48
LastEditors: lmio 2091319361@qq.com
Description: 2454. 下一个更大元素 IV
'''

from collections import defaultdict, deque
from typing import List


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        res, s, t = [-1]*len(nums), [], []
        for i, x in enumerate(nums):
            while t and nums[t[-1]] < x:
                res[t.pop()] = x
            j = len(s) - 1
            while j >= 0 and nums[s[j]] < x:
                j -= 1
            t += s[j + 1:]
            del s[j + 1:]
            s.append(i)
        return res