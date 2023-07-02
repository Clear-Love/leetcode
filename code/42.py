'''
Author: lmio 2091319361@qq.com
Date: 2023-07-02 17:12:09
LastEditors: lmio 2091319361@qq.com
Description: 42. 接雨水
'''
from typing import List

# 动态规划

def trap(height: List[int]) -> int:
    dp = [0] * len(height)
    max_index = 0
    for i in range(1, len(height)):
        if height[i] > height[max_index]:
            j = i-1
            h = height[max_index]
            dp[i] = dp[max_index]
            while j > max_index:
                dp[i] += h - height[j]
                j -= 1
            max_index = i
        else:
            j = i-1
            h = height[i]
            while height[j] < h:
                dp[i] += h - height[j]
                j -= 1
            dp[i] += dp[j]
    return dp[len(height)-1]