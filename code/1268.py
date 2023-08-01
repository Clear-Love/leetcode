'''
Author: lmio 2091319361@qq.com
Date: 2023-07-31 20:03:36
LastEditors: lmio 2091319361@qq.com
Description: 1268. 搜索推荐系统
'''

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if len(node.words) < 3:
                node.words.append(word)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for s in products:
            trie.insert(s)
        node = trie.root
        res = []
        for i, ch in enumerate(searchWord):
            if ch not in node.children:
                return res + [[] for _ in range(len(searchWord)-i)]
            node = node.children[ch]
            res.append(node.words)
        return res