'''
Author: lmio 2091319361@qq.com
Date: 2024-04-09 08:43:30
LastEditors: lmio 2091319361@qq.com
Description: 2529. 正整数和负整数的最大计数
'''


from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
        return max(pos, neg)