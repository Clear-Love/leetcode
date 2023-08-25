'''
Author: lmio 2091319361@qq.com
Date: 2023-08-24 20:50:19
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.15. 最长单词
'''
from typing import List

from utils.trie import Trie

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort(key=lambda x: (-len(x), x))
        for word in words:
            trie.insert(word)
        def isCombo(word: str, havWord: bool) -> bool:
            node = trie.root
            for i, ch in enumerate(word):
                if ch not in node.children:
                    return False
                node = node.children[ch]
                if i < len(word)-1 and node.is_word:
                    if isCombo(word[i+1:], True):
                        return True
            return havWord and node.is_word
        for word in words:
            if isCombo(word, False):
                return word
        return ''