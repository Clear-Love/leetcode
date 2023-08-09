'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 14:37:31
LastEditors: lmio 2091319361@qq.com
Description: 1281. 整数的各位积和之差
'''

from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def get_digits(n: int) -> List[int]:
            digits = []
            while n > 0:
                digit = n % 10
                digits.append(digit)
                n //= 10
            digits.reverse()
            return digits
        dights = get_digits(n)
        x, y = 1, 0
        for v in dights:
            x *= v
            y += v
        return x - y