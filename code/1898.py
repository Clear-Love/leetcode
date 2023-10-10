'''
Author: lmio 2091319361@qq.com
Date: 2023-09-23 16:46:06
LastEditors: lmio 2091319361@qq.com
Description: 1898. 可移除字符的最大数目
'''

from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n, m = len(s), len(p)
        def check(index: int) ->bool:
            rm = set(removable[:index])
            ptr_s, ptr_p = 0, 0
            while ptr_s < n:
                if ptr_s in rm:
                    ptr_s += 1
                    continue
                if s[ptr_s] == p[ptr_p]:
                    ptr_p += 1
                    if ptr_p == m:
                        return True
                ptr_s += 1
            return False
        left, right = 0, len(removable)
        while left < right:
            mid = (left+right+1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid-1
        return left