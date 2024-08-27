'''
Author: lmio 2091319361@qq.com
Date: 2024-05-15 19:12:42
LastEditors: lmio 2091319361@qq.com
Description: 2507. 使用质因数之和替换后可以取到的最小值
'''

class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            x = n
            i = 2
            s = 0
            while i*i <= x:
                while x%i == 0: # 质因数
                    s += i
                    x //= i
                i += 1
            if x > 1:
                s += x
            if s == n:
                return n
            n = s