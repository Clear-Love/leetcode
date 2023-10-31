'''
Author: lmio 2091319361@qq.com
Date: 2023-10-23 13:30:14
LastEditors: lmio 2091319361@qq.com
Description: 2910. 合法分组的最少组数
'''

import math
from typing import Counter, List


class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        cnts = list(cnt.values())
        def check(n: int) ->int:
            ans = 0
            for c in cnts:
                x, y = divmod(c, n)
                if y == 0:
                    ans += x
                elif y+x >= n-1:
                    ans += x+1
                else:
                    return -1
            return ans
        for i in range(min(cnts)+1, 0, -1):
            if (v :=check(i)) != -1:
                return v
        return -1