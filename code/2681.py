'''
Author: lmio 2091319361@qq.com
Date: 2023-08-01 07:18:12
LastEditors: lmio 2091319361@qq.com
Description: 2681. 英雄的力量
'''

from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        mod = 10**9+7
        res, pre = 0, 0
        for num in nums:
            res = (res + num * num * (num + pre)) % mod
            pre = (pre * 2 + num) % mod
        return res