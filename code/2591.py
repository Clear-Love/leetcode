'''
Author: lmio 2091319361@qq.com
Date: 2023-09-22 20:38:23
LastEditors: lmio 2091319361@qq.com
Description: 2591. 将钱分给最多的儿童
'''

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        def check(c: int) ->bool:
            m = money - 8*c
            child = children-c
            if child == 1 and m == 4:
                return False
            if not child and not m:
                return True
            return child and m >= child
        if money < children:
            return -1
        left, right = 0, children
        while left < right:
            mid = (left+right+1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid-1
        return left