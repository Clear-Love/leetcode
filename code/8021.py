'''
Author: lmio 2091319361@qq.com
Date: 2023-08-27 10:52:26
LastEditors: lmio 2091319361@qq.com
Description: 8021. 使子序列的和等于目标的最少操作次数
'''

from functools import cache
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        nums.sort()
        def findSub(arr: List[int], t: int) -> int:
            if not arr:
                return float('inf')
            if arr[0] > t:
                num = arr[0]//2
                a = [num, num]
                return min(findSub(a, t) + 1, findSub(a, target)+1)
            for i, v in enumerate(arr):
                if v == t:
                    return 0
                cnt = findSub(arr[i+1:], t-v)
                if cnt != float('inf'):
                    return cnt
            return float('inf')
        res = findSub(nums, target)
        return  res if res != float('inf') else -1

s = Solution()
print(s.minOperations([1,256,16,128], 3))
