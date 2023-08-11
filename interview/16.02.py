'''
Author: lmio 2091319361@qq.com
Date: 2023-08-10 16:43:34
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.02. 单词频率
'''

from collections import Counter
from typing import List


class WordsFrequency:

    def __init__(self, book: List[str]):
        self.words = Counter(book)

    def get(self, word: str) -> int:
        return self.words[word]