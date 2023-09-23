'''
Author: lmio 2091319361@qq.com
Date: 2023-09-07 09:16:15
LastEditors: lmio 2091319361@qq.com
Description: 1156. 单字符重复子串的最大长度
'''

from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        left, right = 0, 0
        n = len(text)
        cnts = Counter(text)
        res = 0
        while right < n:
            ch = text[left]
            tmpC = cnts[ch]
            while right < n and text[right] == ch:
                cnts[ch] -= 1
                right += 1
            tmpR = right
            # 跳过一次
            if cnts[ch] > 0:
                cnts[ch] -= 1
                right += 1
            while right < n and cnts[ch] > 0 and text[right] == ch:
                right += 1
                cnts[ch] -= 1
            res = max(res, right - left)
            right = tmpR
            left = tmpR
            cnts[ch] = tmpC
        return res