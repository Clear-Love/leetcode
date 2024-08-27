'''
Author: lmio 2091319361@qq.com
Date: 2024-03-13 17:48:00
LastEditors: lmio 2091319361@qq.com
Description: 299. 猜数字游戏
'''

from collections import defaultdict
from typing import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnts = Counter(secret)
        a, b = 0, 0
        cb = defaultdict(int)
        for i in range(len(secret)):
            w = guess[i]
            if w in cnts:
                if w == secret[i]:
                    a += 1
                else:
                    b += 1
                    cb[w] += 1
                cnts[guess[i]] -= 1
                if cnts[guess[i]] == 0:
                    del cnts[guess[i]]
            elif w in cb and w == secret[i]:
                cb[w] -= 1
                a += 1
                b -= 1
                if cb[w] == 0:
                    del cb[w]
        return str(a) + 'A' + str(b) + 'B'