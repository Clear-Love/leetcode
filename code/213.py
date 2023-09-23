'''
Author: lmio 2091319361@qq.com
Date: 2023-09-17 18:53:18
LastEditors: lmio 2091319361@qq.com
Description: 213. 打家劫舍 II
'''

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def f(arr: List[int]) -> int:
            if not arr:
                return 0
            n = len(arr)
            if n == 1:
                return arr[0]
            dp = [0]*n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-2]+arr[i], dp[i-1])
            return dp[-1]
        return max(f(nums[1:]), f(nums[:len(nums)-1]))