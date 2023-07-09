'''
Author: lmio 2091319361@qq.com
Date: 2023-07-09 10:36:48
LastEditors: lmio 2091319361@qq.com
Description: 6899. 达到末尾下标所需的最大跳跃次数
'''

from typing import List


def maximumJumps(nums: List[int], target: int) -> int:
    if target == 0:
        return -1
    dp = [-1]*len(nums)
    dp[0] = 0
    for i in range(1, len(nums)):
        j = i -1
        while j >= 0:
            if dp[j] == -1 or abs(nums[j] - nums[i]) > target:
                j -= 1
                continue
            dp[i] = max(dp[j]+1, dp[i])
            j -= 1
    return dp[-1]

print(maximumJumps([1,3,6,4,1,2], 2))