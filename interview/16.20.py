'''
Author: lmio 2091319361@qq.com
Date: 2023-08-17 19:13:54
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.20. T9键盘
'''

from typing import List

from utils.trie import Trie, TrieNode


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        key_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        tire = Trie()
        for word in words:
            tire.insert(word)
        res = []
        path = []
        n = len(num)
        def dfs(k: int, node: TrieNode):
            if k == n:
                if node.is_word:
                    res.append(''.join(path))
                return
            for ch in key_map[num[k]]:
                if ch in node.children:
                    path.append(ch)
                    dfs(k+1, node.children[ch])
                    path.pop()
        dfs(0, tire.root)
        return res