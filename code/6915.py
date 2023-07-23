'''
Author: lmio 2091319361@qq.com
Date: 2023-07-23 10:34:05
LastEditors: lmio 2091319361@qq.com
Description: 6915. 合并后数组中的最大元素
'''

from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = nums[-1]
        current_sum = nums[-1]
        
        for i in range(n-2, -1, -1):
            if current_sum >= nums[i]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_value = max(max_value, current_sum)
        return max_value

s = Solution()
print(s.maxArrayValue([5,3,3]))