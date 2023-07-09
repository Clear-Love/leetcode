'''
Author: lmio 2091319361@qq.com
Date: 2023-07-09 11:05:20
LastEditors: lmio 2091319361@qq.com
Description: 6912. 构造最长非递减子数组
'''

from typing import List

def maxNonDecreasingLength(nums1: List[int], nums2: List[int]) -> int:
    if len(nums1) == 0:
        return []
    dp = [[1, 1] for _ in range(len(nums1))]
    res = 1
    for i in range(1, len(nums1)):
        v1, v2 = nums1[i], nums2[i]
        if v1 >= nums1[i-1]:
            dp[i][0] = dp[i-1][0] + 1
        if v1 >= nums2[i-1]:
            dp[i][0] = max(dp[i][0], dp[i-1][1]+1)
        if v2 >= nums1[i-1]:
            dp[i][1] = dp[i-1][0] + 1
        if v2 >= nums2[i-1]:
            dp[i][1] = max(dp[i][1], dp[i-1][1]+1)
        res = max(res, dp[i][0], dp[i][1])
    return res

print(maxNonDecreasingLength([2,3,1], [1,2,1]))