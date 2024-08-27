'''
Author: lmio 2091319361@qq.com
Date: 2024-03-21 13:49:45
LastEditors: lmio 2091319361@qq.com
Description: 1969. 数组元素的最小非零乘积
'''

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 1_000_000_007
        k = (1 << p) - 1
        return k * pow(k - 1, k >> 1, MOD) % MOD