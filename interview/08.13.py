'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 16:02:14
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.13. 堆箱子
'''

from typing import List


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        n = len(box)
        dp = [0] * n
        box.sort(key=lambda x: x[0])
        for i in range(n):
            dp[i] = box[i][2]
            for j in range(i):
                if all(box[i][k] > box[j][k] for k in range(0,3)):
                    dp[i] = max(dp[i], dp[j] + box[i][2])
        return max(dp)