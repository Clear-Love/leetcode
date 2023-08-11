'''
Author: lmio 2091319361@qq.com
Date: 2023-08-10 16:22:58
LastEditors: lmio 2091319361@qq.com
Description: 面试题 10.11. 峰与谷
'''

from ast import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        for i in range(1, len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]