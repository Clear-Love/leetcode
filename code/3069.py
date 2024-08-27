'''
Author: lmio 2091319361@qq.com
Date: 2024-03-04 16:09:03
LastEditors: lmio 2091319361@qq.com
Description: 3069. 将元素分配到两个数组中 I
'''

from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1, arr2 = [nums[0]], [nums[1]]
        for i in range(2, n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2