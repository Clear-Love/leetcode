'''
Author: lmio 2091319361@qq.com
Date: 2024-03-16 18:50:08
LastEditors: lmio 2091319361@qq.com
Description: 1696. 跳跃游戏 VI
'''

from collections import deque
from math import inf
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        q = deque([0])
        for i in range(1, n):
            if q[0] < i-k:
                q.popleft()
            dp[i] = dp[q[0]]+nums[i]
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)
        return dp[-1]