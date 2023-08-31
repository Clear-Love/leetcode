'''
Author: lmio 2091319361@qq.com
Date: 2023-08-30 21:32:12
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.25. 单词矩阵
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

class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        area = 0
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(arr: List[TrieNode], path: List[str]):
            for word in words:
                if len(word) != len(arr):
                    continue
                for i, c in enumerate(word):
                    if c not in arr[i].children:
                        break
                else:
                    flag = True
                    temp = arr.copy()
                    # 若全部为单词结尾
                    for i, c in enumerate(word):
                        temp[i] = temp[i].children[c]
                        flag &= temp[i].is_word
                    path.append(word)
                    if flag:
                        h, w = len(path), len(word)
                        nonlocal area, res
                        if h * w > area:
                            area = h * w
                            res = path.copy()
                    dfs(temp, path)
                    path.pop()
        # 枚举单词长度
        ll = sorted(set(len(word) for word in words), reverse = True)
        for l in ll:
            if l * ll[0] < area:
                break
            dfs([trie.root] * l, [])
        return res