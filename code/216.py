'''
Author: lmio 2091319361@qq.com
Date: 2023-10-26 00:25:15
LastEditors: lmio 2091319361@qq.com
Description: 316. 去除重复字母
'''

from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnts = Counter(s)
        res = []
        in_res = set()
        for ch in s:
            cnts[ch] -= 1
            if ch in in_res:
                continue
            while res and ch < res[-1] and cnts[res[-1]]:
                in_res.remove(res.pop())
            res.append(ch)
            in_res.add(ch)
        return ''.join(res)