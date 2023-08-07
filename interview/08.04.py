'''
Author: lmio 2091319361@qq.com
Date: 2023-08-07 15:54:28
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.04. 幂集
'''

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        def braceback(i: int):
            res.append(path.copy())
            if i == n:
                return
            for j in range(i, n):
                path.append(nums[j])
                braceback(j+1)
                path.pop()
        braceback(0)
        return res