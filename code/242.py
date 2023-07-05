'''
Author: lmio 2091319361@qq.com
Date: 2023-07-05 22:15:19
LastEditors: lmio 2091319361@qq.com
Description: 242. 有效的字母异位词
'''

from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)