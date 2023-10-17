'''
Author: lmio 2091319361@qq.com
Date: 2023-10-16 23:23:05
LastEditors: lmio 2091319361@qq.com
Description: 260. 只出现一次的数字 III
'''

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        key = xor_sum&-xor_sum
        n1, n2 = 0, 0
        for num in nums:
            if num&key:
                n1 ^= num
            else:
                n2 ^= num
        return [n1, n2]