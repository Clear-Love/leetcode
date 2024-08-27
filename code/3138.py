'''
Author: lmio 2091319361@qq.com
Date: 2024-05-06 16:15:55
LastEditors: lmio 2091319361@qq.com
Description: 3138. 同位字符串连接的最小长度
'''

from typing import Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        cnts = Counter()
        def check(word: str) -> bool:
            c = Counter()
            for w in word:
                if w not in cnts:
                    return False
                c[w] += 1
                if c[w] > cnts[w]:
                    return False
            return True
        for k in range(1, n):
            if n%k != 0:
                continue
            cnts = Counter(s[:k])
            f = True
            for i in range(k, n-k+1, k):
                if not check(s[i:i+k]):
                    f = False
                    break
            if f:
                return k
        return n