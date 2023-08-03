'''
Author: lmio 2091319361@qq.com
Date: 2023-08-02 22:52:16
LastEditors: lmio 2091319361@qq.com
Description: 2763. 所有子数组中不平衡数字之和
'''
from typing import List


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        for i, x in enumerate(nums):
            visited = [False] * (n + 2)
            visited[x] = True
            cnt = 0
            for j in range(i + 1, n):
                x = nums[j]
                if not visited[x]:
                    cnt += 1 - visited[x - 1] - visited[x + 1]
                    visited[x] = True
                res += cnt
        return res