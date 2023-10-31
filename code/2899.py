'''
Author: lmio 2091319361@qq.com
Date: 2023-10-20 11:52:19
LastEditors: lmio 2091319361@qq.com
Description: 2899. 上一个遍历的整数
'''

from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        res = []
        stack = []
        prevCnt = 0
        for word in words:
            if word == 'prev':
                prevCnt += 1
                if prevCnt > len(stack):
                    res.append(-1)
                else:
                    res.append(stack[-prevCnt])
            else:
                prevCnt = 0
                stack.append(int(word))
        return res