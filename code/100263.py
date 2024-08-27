'''
Author: lmio 2091319361@qq.com
Date: 2024-03-31 10:37:33
LastEditors: lmio 2091319361@qq.com
Description: 100263. 哈沙德数
'''

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        tmp = x
        while tmp:
            s += tmp%10
            tmp = tmp//10
        return -1 if x%s else s

print(Solution().sumOfTheDigitsOfHarshadNumber(18))