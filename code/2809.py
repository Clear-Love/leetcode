'''
Author: lmio 2091319361@qq.com
Date: 2024-01-20 17:11:46
LastEditors: lmio 2091319361@qq.com
Description: 2809. 使数组和小于等于 x 的最少时间
'''

from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        # 按nums2 从小到大排序
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1])
        n = len(nums1)
        s1, s2 = sum(nums1), sum(nums2)
        # dp[i+1][j] = max(dp[i][j], dp[i][j-1]+nums1[i]+nums2[i]*J), dp[0][0] = 0
        dp = [0]*(n+1)
        for i, (a, b) in enumerate(pairs):
            for j in range(i+1, 0, -1):
                dp[j] = max(dp[j], dp[j-1]+a+b*j)
        for t, v in enumerate(dp):
            if s1 + s2*t - v <= x:
                return t
        return -1