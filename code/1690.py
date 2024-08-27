'''
Author: lmio 2091319361@qq.com
Date: 2024-03-16 16:17:27
LastEditors: lmio 2091319361@qq.com
Description: 1690. 石子游戏 VII
'''

from itertools import accumulate
from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        preSum = list(accumulate(stones, initial=0))
        # 0偶数，1奇数
        key = n%2
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for d in range(1, n):
            for i in range(n-d):
                j = i+d
                if d%2 != key:
                    # alice选，扩大得分差值
                    dp[i][j] = max(preSum[j+1]-preSum[i+1]+dp[i+1][j], preSum[j]-preSum[i]+dp[i][j-1])
                else:
                    dp[i][j] = min(-preSum[j+1]+preSum[i+1]+dp[i+1][j], -preSum[j]+preSum[i]+dp[i][j-1])
        return dp[0][-1]

print(Solution().stoneGameVII([5, 3,1,4,2]))