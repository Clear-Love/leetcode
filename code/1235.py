'''
Author: lmio 2091319361@qq.com
Date: 2023-08-20 21:22:24
LastEditors: lmio 2091319361@qq.com
Description: 1235. 规划兼职工作
'''

import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        works = sorted(zip(endTime, startTime, profit))
        n = len(works)
        dp = [0]*(n+1)
        for i, (_, start, gold) in enumerate(works, start=1):
            j = bisect.bisect_right(works, start, hi=i, key=lambda x: x[0])
            dp[i] = max(dp[i-1], dp[j] + gold)
        return dp[-1]