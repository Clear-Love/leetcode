'''
Author: lmio 2091319361@qq.com
Date: 2023-09-30 22:30:29
LastEditors: lmio 2091319361@qq.com
Description: 8038. 收集元素的最少操作次数
'''

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m = set([i for i in range(1, k+1)])
        res = 0
        while nums:
            res += 1
            num = nums.pop()
            if num in m:
                m.remove(num)
                if len(m) == 0:
                    return res
        return res