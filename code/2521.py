'''
Author: lmio 2091319361@qq.com
Date: 2024-05-15 19:25:56
LastEditors: lmio 2091319361@qq.com
Description: 2521. 数组乘积中的不同质因数数目
'''

from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        acc = 1
        for num in nums:
            acc *= num
        s = set()
        i = 2
        while i * i <= acc:
            if acc % i == 0:
                s.add(i)
            while acc % i == 0:
                acc //= i
            i += 1
        if acc > 1:
            s.add(acc)
        return len(s)