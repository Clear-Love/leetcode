'''
Author: lmio 2091319361@qq.com
Date: 2023-10-01 10:43:00
LastEditors: lmio 2091319361@qq.com
Description:100086. 有序三元组中的最大值 I 
'''

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        # 计算前缀最小值和后缀最大值
        prefix_max = [float('-inf')] * n
        suffix_max = [float('-inf')] * n
        prefix_max[0] = nums[0]
        suffix_max[-1] = nums[-1]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], nums[i])
        res = 0
        # 遍历数组，计算最大值
        for j in range(1, n-1):
            product = (prefix_max[j-1] - nums[j]) * suffix_max[j+1]
            res = max(res, product)
        return res