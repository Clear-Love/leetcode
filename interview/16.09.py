'''
Author: lmio 2091319361@qq.com
Date: 2023-08-12 21:03:06
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.09. 运算
'''

class Operations:
    def __init__(self):
        pass

    def minus(self, a: int, b: int) -> int:
        return a-b


    def multiply(self, a: int, b: int) -> int:
        return a*b


    def divide(self, a: int, b: int) -> int:
        if (a < 0) ^ (b < 0):
            return -self.divide(abs(a), abs(b))
        return a//b