'''
Author: lmio 2091319361@qq.com
Date: 2023-08-31 19:34:18
LastEditors: lmio 2091319361@qq.com
Description: 75. 颜色分类
'''

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        left, right = 0, n-1
        i = 0
        while i <= right:
            while i <= right and nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            i += 1