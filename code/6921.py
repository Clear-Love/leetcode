'''
Author: lmio 2091319361@qq.com
Date: 2023-07-23 10:30:28
LastEditors: lmio 2091319361@qq.com
Description: 6921. 按分隔符拆分字符串
'''

from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            split_words = word.split(separator)
            for split_word in split_words:
                if split_word != '':
                    res.append(split_word)
        return res