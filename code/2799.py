'''
Author: lmio 2091319361@qq.com
Date: 2023-08-01 08:07:18
LastEditors: lmio 2091319361@qq.com
Description: 2799. 统计完全子数组的数目
'''

from collections import Counter
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnts = set(nums)
        n = len(nums)
        cnt = len(cnts)
        left, right = 0, cnt-1
        cnts = Counter(nums[:cnt])
        res = 0
        while right < len(nums):
            while len(cnts) == cnt:
                res += n-right
                cnts[nums[left]] -= 1
                if cnts[nums[left]] == 0:
                    cnts.pop(nums[left])
                left += 1
            right += 1
            if right < len(nums):
                cnts[nums[right]] += 1
        return res