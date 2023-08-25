'''
Author: lmio 2091319361@qq.com
Date: 2023-08-24 23:20:09
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.18. 最短超串
'''

from collections import Counter, defaultdict
from typing import List


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        t = set(small)
        k = len(small)
        dic = defaultdict(int)
        l, r = 0, 0
        res = []
        while r < len(big):
            if big[r] in t:
                dic[big[r]] +=1
            while len(dic) == k:
                if not res or  r - l < res[1] - res[0]:
                    res = [l, r]
                if big[l] in t:
                    dic[big[l]] -=1
                if dic[big[l]] == 0:
                    dic.pop(big[l])
                l +=1
            r +=1
        return res

s = Solution()
print(s.shortestSeq([7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7], [1, 5, 9]))