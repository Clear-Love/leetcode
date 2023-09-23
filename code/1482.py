'''
Author: lmio 2091319361@qq.com
Date: 2023-09-22 21:40:22
LastEditors: lmio 2091319361@qq.com
Description: 1482. 制作 m 束花所需的最少天数
'''

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        def check(day: int) ->bool:
            cnt = 0
            flowers = 0
            for v in bloomDay:
                if v > day:
                    cnt = 0
                    continue
                cnt += 1
                if cnt == k:
                    cnt = 0
                    flowers += 1
                    if flowers >= m:
                        return True
            return False
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left+right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left