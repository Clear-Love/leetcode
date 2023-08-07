'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 19:42:15
LastEditors: lmio 2091319361@qq.com
Description: 面试题 05.01. 插入
'''

class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        H = (((1 << (j+1)) -1) >> i) << i
        N &= ~H
        return N | (M << i)&H