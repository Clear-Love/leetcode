'''
Author: lmio 2091319361@qq.com
Date: 2023-08-13 11:05:14
LastEditors: lmio 2091319361@qq.com
Description: 7022. 限制条件下元素之间的最小绝对差
'''

from typing import List


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sn = sorted(((v, i) for i, v in enumerate(nums)))
        res = float('inf')
        for i in range(1, len(sn)):
            j = i
            while j >= 0 and abs(sn[i][1] - sn[j][1]) < x:
                j -= 1
            if j != -1:
                res = min(res, sn[i][0]-sn[j][0])
        return res