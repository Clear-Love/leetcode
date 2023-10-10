'''
Author: lmio 2091319361@qq.com
Date: 2023-09-30 17:37:57
LastEditors: lmio 2091319361@qq.com
Description: 2841. 几乎唯一子数组的最大和
'''

from collections import Counter
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        arr = Counter(nums[:k])
        s = sum(nums[:k])
        left, right = 0, k
        n = len(nums)
        res = 0 if len(arr) < m else s
        while right < n:
            arr[nums[right]] += 1
            arr[nums[left]] -= 1
            if not arr[nums[left]]:
                arr.pop(nums[left])
            s += nums[right]-nums[left]
            if len(arr) >= m:
                res = max(res, s)
            left += 1
            right += 1
        return res