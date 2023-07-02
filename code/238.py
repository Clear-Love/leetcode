'''
Author: lmio 2091319361@qq.com
Date: 2023-07-02 15:36:31
LastEditors: lmio 2091319361@qq.com
Description: 238. 除自身以外数组的乘积
'''
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    res, lsum, rsum = [1] * len(nums), 1, 1
    for i in range(len(nums)-1):
        lsum *= nums[i]
        res[i+1] = lsum
    for i in range(len(nums)-1, 0, -1):
        rsum *= nums[i]
        res[i-1] *= rsum
    return res