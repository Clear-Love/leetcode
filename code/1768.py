'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 16:51:30
LastEditors: lmio 2091319361@qq.com
Description: 1768. 交替合并字符串
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        isOne = True
        res = []
        while i < len(word1) and j < len(word2):
            if isOne:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
            isOne = not isOne
        if i >= len(word1):
            res += word2[j:]
        else:
            res += word1[i:]
        return ''.join(res)
