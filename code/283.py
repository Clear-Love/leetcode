'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 20:18:36
LastEditors: lmio 2091319361@qq.com
Description: 283. 移动零
'''

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        rp, wp = 0, 0
        while rp < len(nums):
            val = nums[rp]
            if val != 0:
                nums[wp] = val
                wp += 1
            rp += 1
        while wp < len(nums):
            nums[wp] = 0
            wp += 1