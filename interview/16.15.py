'''
Author: lmio 2091319361@qq.com
Date: 2023-08-15 22:12:07
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.15. 珠玑妙算
'''

from collections import Counter, defaultdict
from typing import List


class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        s = Counter(solution)
        fake = 0
        bingo = 0
        for v in guess:
            if v in s:
                if s[v] > 0:
                    fake += 1
                    s[v] -= 1
        for i, v in enumerate(guess):
            if v == solution[i]:
                fake -= 1
                bingo += 1
        return [bingo, fake]