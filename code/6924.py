'''
Author: lmio 2091319361@qq.com
Date: 2023-07-16 19:53:52
LastEditors: lmio 2091319361@qq.com
Description: 6924. 最长合法子字符串的长度
'''
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> int:
        node = self.root
        for i, ch in enumerate(word):
            if node.is_word:
                return i-1
            if ch not in node.children:
                return len(word)
            node = node.children[ch]
        return len(word)-1 if node.is_word else len(word)


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        trie = Trie()
        for w in forbidden:
            trie.insert(w)
        dp = [0]*n
        dp[n-1] = trie.search(word[n-1])
        for i in range(n-2, -1, -1):
            dp[i] = trie.search(word[i:i+dp[i+1]+1])
        print(dp)
        return max(dp)