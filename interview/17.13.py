'''
Author: lmio 2091319361@qq.com
Date: 2023-08-22 19:50:18
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.13. 恢复空格
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

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class Solution:
    def respace(self, dictionary: List[str], s: str) -> int:
        # 构建前缀树
        word_tree = Trie()
        for w in dictionary:
            word_tree.insert(w)
        n = len(s)
        dp=[n-i for i in range(n+1)]
        for i in range(n-1, -1, -1):
            node = word_tree.root
            for j in range(i, n):
                ch = s[j]
                if ch not in node.children:
                    dp[i] = min(dp[i], dp[j+1] + j-i+1)
                    break
                node = node.children[ch]
                if node.is_word:
                    dp[i] = min(dp[i], dp[j+1])
                else:
                    dp[i] = min(dp[i], dp[i+1] + j-i+1)
        return dp[0]