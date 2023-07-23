'''
Author: lmio 2091319361@qq.com
Date: 2023-07-23 11:05:19
LastEditors: lmio 2091319361@qq.com
Description: 6955. 长度递增组的最大数目
'''

from typing import List


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        res = 0
        # 最小满足剩余
        curr = 0
        for v in usageLimits:
            curr += v
            # 可使用次数至少为长度加一
            if curr > res:
                res += 1
                curr -= res
        return res