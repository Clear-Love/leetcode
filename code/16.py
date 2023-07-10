'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 12:42:16
LastEditors: lmio 2091319361@qq.com
Description: 16. 最接近的三数之和
'''

import bisect
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    gap = float('inf')
    res = 0
    for i in range(n):
        for j in range(i+1, n-1):
            sum = nums[i] + nums[j]
            sum += findClosest(nums[j+1:], target-sum)
            _gap = abs(target - sum)
            if _gap < gap:
                gap = _gap
                res = sum
    return res

def findClosest(nums: List[int], target: int):
    insert_pos = bisect.bisect_left(nums, target)
    
    if insert_pos == 0:
        return nums[0]
    elif insert_pos == len(nums):
        return nums[-1]
    else:
        left_diff = abs(target - nums[insert_pos - 1])
        right_diff = abs(target - nums[insert_pos])
        
        if left_diff <= right_diff:
            return nums[insert_pos - 1]
        else:
            return nums[insert_pos]

print(threeSumClosest([1,1,1,0], -100))