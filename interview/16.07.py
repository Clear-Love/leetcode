'''
Author: lmio 2091319361@qq.com
Date: 2023-08-11 16:53:44
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.07. 最大数值
'''

class Solution:
    def maximum(self, a: int, b: int) -> int:
        return ((a + b) + abs(a - b)) // 2