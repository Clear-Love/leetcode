'''
Author: lmio 2091319361@qq.com
Date: 2023-08-06 10:35:15
LastEditors: lmio 2091319361@qq.com
Description: 6953. 判断是否能拆分数组
'''

from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        preSum = []
        sum = 0
        for v in nums:
            sum += v
            preSum.append(sum)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for d in range(1, n):
            for i in range(n):
                if i + d >= n:
                    break
                j = i + d
                for k in range(i, i+d):
                    if dp[i][k] and dp[k+1][j]:
                        dp[i][j] = True
                        break
                if i == 0 and j == n-1:
                    continue
                dp[i][j] = dp[i][j] and (preSum[j] - (preSum[i-1] if i > 0 else 0)) >= m
        return dp[0][n-1]

s = Solution()
print(s.canSplitArray([1, 1], 4))