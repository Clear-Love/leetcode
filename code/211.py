'''
Author: lmio 2091319361@qq.com
Date: 2023-07-14 15:44:52
LastEditors: lmio 2091319361@qq.com
Description: 
'''

from utils.trie import TrieNode


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.root)

    def searchHelper(self, word: str, node: TrieNode) -> bool:
        if not word:
            return node.is_word
        ch = word[0]
        if ch == '.':
            for child in node.children.values():
                if self.searchHelper(word[1:], child):
                    return True
        elif ch in node.children:
                return self.searchHelper(word[1:], node.children[ch])
        return False