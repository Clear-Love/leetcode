'''
Author: lmio 2091319361@qq.com
Date: 2023-07-15 19:53:42
LastEditors: lmio 2091319361@qq.com
Description:172. 阶乘后的零 
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count