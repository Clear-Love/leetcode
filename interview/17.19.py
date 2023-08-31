'''
Author: lmio 2091319361@qq.com
Date: 2023-08-25 22:56:07
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.19. 消失的两个数字
'''

from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        xorsum = 0
        n = len(nums) + 2
        for num in nums:
            xorsum ^= num
        for i in range(1, n + 1):
            xorsum ^= i
        # 找到最低有效位1，xorsum是消失数字的异或结果，代表这两个数在这一位不同
        lsb = xorsum & (-xorsum)
        num1 = num2 = 0
        for num in nums:
            if num & lsb:
                num1 ^= num
            else:
                num2 ^= num
        for i in range(1, n + 1):
            if i & lsb:
                num1 ^= i
            else:
                num2 ^= i
        return [num1, num2]

