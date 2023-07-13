'''
Author: lmio 2091319361@qq.com
Date: 2023-07-12 23:12:31
LastEditors: lmio 2091319361@qq.com
Description: 
'''
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum = 0
        flag = 1
        while n:
            q, r = divmod(n, 10)
            sum += flag*r
            n = q
        if flag == -1:
            return -sum
        return sum