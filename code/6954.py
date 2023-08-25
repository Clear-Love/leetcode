'''
Author: lmio 2091319361@qq.com
Date: 2023-08-19 22:34:02
LastEditors: lmio 2091319361@qq.com
Description: 6954. 统计和小于目标的下标对数目
'''

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    count += 1
                else:
                    break
        return count