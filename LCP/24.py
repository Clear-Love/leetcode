'''
Author: lmio 2091319361@qq.com
Date: 2024-03-13 20:45:46
LastEditors: lmio 2091319361@qq.com
Description: LCP 24. 数字游戏
'''

import heapq
from typing import List


class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        MOD = 10**9+7
        left, right = [], []
        lSum, rSum = 0, 0
        res = []
        for i, v in enumerate(nums):
            v -= i
            # 偶数
            if i&1 == 0:
                x = -heapq.heappushpop(left, -v)
                heapq.heappush(right, x)
                lSum += v-x
                rSum += x
                res.append((rSum-lSum-right[0])%MOD)
            else:
                x = heapq.heappushpop(right, v)
                heapq.heappush(left, -x)
                lSum += x
                rSum += v-x
                res.append((rSum-lSum)%MOD)
        return res