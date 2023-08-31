'''
Author: lmio 2091319361@qq.com
Date: 2023-08-27 10:43:38
LastEditors: lmio 2091319361@qq.com
Description: 8022. 找出美丽数组的最小和
'''

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        res = 0
        i = 1
        ban = set()
        for _ in range(n):
            while i in ban:
                i += 1
            ban.add(target - i)
            res += i
            i += 1
        return res