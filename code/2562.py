'''
Author: lmio 2091319361@qq.com
Date: 2023-10-12 21:01:20
LastEditors: lmio 2091319361@qq.com
Description: 2562. 找出数组的串联值
'''

from collections import deque
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        q = deque(nums)
        res = 0
        while q:
            if len(q) == 1:
                res += q.pop()
            else:
                res += int(str(q.popleft()) + str(q.pop()))
        return res