'''
Author: lmio 2091319361@qq.com
Date: 2023-07-05 21:36:18
LastEditors: lmio 2091319361@qq.com
Description: 383. 赎金信
'''

from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    letter = Counter(magazine)
    for ch in ransomNote:
        if ch not in letter:
            return False
        letter[ch] -= 1
        if letter[ch] == 0:
            del letter[ch]
    return True
