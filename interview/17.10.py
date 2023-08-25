'''
Author: lmio 2091319361@qq.com
Date: 2023-08-22 16:31:54
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.10. 主要元素
'''

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = -1
        cnt = 0
        for num in nums:
            if not cnt:
                major = num
            if num != major:
                cnt -= 1
            else:
                cnt += 1
        return major if nums.count(major) > len(nums)//2 else -1