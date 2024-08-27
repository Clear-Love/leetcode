'''
Author: lmio 2091319361@qq.com
Date: 2024-03-09 14:11:18
LastEditors: lmio 2091319361@qq.com
Description: 2386. 找出数组的第 K 大和
'''

import heapq
from itertools import accumulate
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        sum = 0
        for i, x in enumerate(nums):
            if x >= 0:
                sum += x
            else:
                nums[i] = -x
        nums.sort()

        h = [(0, 0)]  # 空子序列
        for _ in range(k - 1):
            s, i = heapq.heappop(h)
            if i < len(nums):
                # 在子序列的末尾添加 nums[i]
                heapq.heappush(h, (s + nums[i], i + 1))  # 下一个添加/替换的元素下标为 i+1
                if i:  # 替换子序列的末尾元素为 nums[i]
                    heapq.heappush(h, (s + nums[i] - nums[i - 1], i + 1))
        return sum - h[0][0]

print(Solution().kSum([1, -2,3,4,-10,12], 16))