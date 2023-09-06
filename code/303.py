'''
Author: lmio 2091319361@qq.com
Date: 2023-09-02 15:54:56
LastEditors: lmio 2091319361@qq.com
Description: 303. 区域和检索 - 数组不可变
'''

from itertools import accumulate
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.preSum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right] - self.preSum[left] + self.arr[left]