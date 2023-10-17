'''
Author: lmio 2091319361@qq.com
Date: 2023-10-17 15:38:22
LastEditors: lmio 2091319361@qq.com
Description: 2652. 倍数求和
'''

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def f(m: int) -> int:
            return (m + n // m * m) * (n // m) // 2
        return f(3) + f(5) + f(7) - f(3 * 5) - f(3 * 7) - f(5 * 7) + f(3 * 5 * 7)