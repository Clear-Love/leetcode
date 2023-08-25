'''
Author: lmio 2091319361@qq.com
Date: 2023-08-20 16:17:46
LastEditors: lmio 2091319361@qq.com
Description: 6467. 找出最长等值子数组
'''

from collections import defaultdict
from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = [[] for _ in range(len(nums) + 1)]
        for i, v in enumerate(nums):
            pos[v].append(i - len(pos[v]))
        res = 0
        for ps in pos:
            left = 0
            for right, p in enumerate(ps):
                # 删除中间的数
                while p - ps[left] > k:
                    left += 1
                res = max(res, right - left + 1)
        return res