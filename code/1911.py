'''
Author: lmio 2091319361@qq.com
Date: 2023-07-11 18:41:34
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # 结尾为奇数位
        odd = 0
        # 结尾为偶数位
        even = 0
        for _, x in enumerate(nums, 1):
            odd = max(even - x, odd)
            even = max(odd + x, even)
        return max(odd, even)