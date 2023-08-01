'''
Author: lmio 2091319361@qq.com
Date: 2023-07-31 16:50:04
LastEditors: lmio 2091319361@qq.com
Description: 1318. 或运算的最小翻转次数
'''

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            bit_a, bit_b, bit_c = a&1, b&1, c&1
            if bit_a | bit_b == bit_c:
                pass
            elif bit_a & bit_b == 1:
                res += 2
            else:
                res += 1
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return res