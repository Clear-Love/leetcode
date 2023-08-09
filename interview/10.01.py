'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 21:55:56
LastEditors: lmio 2091319361@qq.com
Description: 面试题 10.01. 合并排序的数组
'''

from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        rA, rB, wp = m-1, n-1, m+n-1
        while wp >= 0:
            if rA >= 0 and (rB < 0 or A[rA] > B[rB]):
                A[wp] = A[rA]
                rA -= 1
            else:
                A[wp] = B[rB]
                rB -= 1
            wp -= 1