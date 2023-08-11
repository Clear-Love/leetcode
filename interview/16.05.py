'''
Author: lmio 2091319361@qq.com
Date: 2023-08-11 16:31:31
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.05. 阶乘尾数
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            n = n // 5
            res += n
        return res