'''
Author: lmio 2091319361@qq.com
Date: 2023-08-07 16:06:32
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.05. 递归乘法
'''

class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A < B:
            A, B = B, A
        if B == 1:
            return A
        return (self.multiply(A, B>>1) << 1) + A if B & 1 else \
            self.multiply(A, B>>1) << 1