'''
Author: lmio 2091319361@qq.com
Date: 2023-08-19 20:04:20
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.08. 马戏团人塔
'''

import bisect
from typing import List


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        people = list(zip(height, weight))
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        dp = [people[0][1]]
        for i in range(1, n):
            w = people[i][1]
            if w > dp[-1]:
                dp.append(w)
            else:
                idx = bisect.bisect_left(dp, w)
                dp[idx] = w
        return len(dp)