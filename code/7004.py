'''
Author: lmio 2091319361@qq.com
Date: 2023-08-20 10:44:36
LastEditors: lmio 2091319361@qq.com
Description: 7004. 判别首字母缩略词
'''

from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        w = []
        for word in words:
            w.append(word[0])
        return ''.join(w) == s