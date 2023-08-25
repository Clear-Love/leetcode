'''
Author: lmio 2091319361@qq.com
Date: 2023-08-20 22:57:42
LastEditors: lmio 2091319361@qq.com
Description: 2054. 两个最好的不重叠活动
'''

import bisect
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[0 for _ in range(3)] for _ in range(n+1)]
        for i, (start, _, gold) in enumerate(events, start=1):
            j = bisect.bisect_left(events, start, hi=i, key=lambda x: x[1])
            for c in range(1, 3):
                dp[i][c] = max(dp[i-1][c], dp[j][c-1] + gold)
        return dp[-1][-1]