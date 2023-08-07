'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 22:03:34
LastEditors: lmio 2091319361@qq.com
Description: 面试题 05.06. 整数转换
'''

class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        res = 0
        for _ in range(32):
            if A&1 ^ B&1:
                res += 1
            A = A >> 1
            B = B >> 1
        return res