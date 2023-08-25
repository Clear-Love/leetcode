'''
Author: lmio 2091319361@qq.com
Date: 2023-08-20 22:44:25
LastEditors: lmio 2091319361@qq.com
Description: 1751. 最多可以参加的会议数目 II
'''

import bisect
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        for i, (start, _, gold) in enumerate(events, start=1):
            j = bisect.bisect_right(events, start-1, hi=i, key=lambda x: x[1])
            for c in range(1, k+1):
                dp[i][c] = max(dp[i-1][c], dp[j][c-1] + gold)
        return dp[-1][-1]