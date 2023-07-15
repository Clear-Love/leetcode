'''
Author: lmio 2091319361@qq.com
Date: 2023-07-15 02:42:04
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(start: int, tar: int):
            m = set()
            r = set()
            for i in range(start, len(nums)):
                v = nums[i]
                y = tar - v
                if y in m:
                    r.add((y, v))
                m.add(v)
            return r
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                    if j > i+1 and nums[j] == nums[j-1]:
                        continue
                    sum = nums[i] + nums[j]
                    twoNum = twoSum(j+1, target-sum)
                    for v in twoNum:
                        res.append([nums[i], nums[j], v[0], v[1]])
        return res