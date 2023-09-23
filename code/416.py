'''
Author: lmio 2091319361@qq.com
Date: 2023-09-16 18:28:05
LastEditors: lmio 2091319361@qq.com
Description: 416. 分割等和子集
'''

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:      # 总和无法等分
            return False
        
        target = total // 2
        if max(nums) > target:  # 最大值大于总和的一半，无法分割
            return False
        
        '''【0/1背包】：从nums中选出的数字刚好能组成target'''
        n = len(nums)

        # 初始化
        dp = [[False] * (target+1) for _ in range(n+1)]
        # dp[i][j]: 从前i个元素中选出若干个数字刚好能够组成j
        dp[0][0] = True     # 其他 dp[0][j]均为False

        # 状态更新
        for i in range(1, n+1):
            for j in range(target+1):
                if j < nums[i-1]:   # 容量有限，无法选择第i个数字nums[i-1]
                    dp[i][j] = dp[i-1][j]
                else:               # 可选择第i个数字nums[i-1]，也可不选
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
        
        return dp[n][target]