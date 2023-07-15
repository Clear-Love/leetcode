'''
Author: lmio 2091319361@qq.com
Date: 2023-07-14 16:00:34
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from typing import List
from utils.trie import Trie, TrieNode

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        words = set(words)
        if not board:
            return []
        n, m = len(board), len(board[0])
        for word in words:
            trie.insert(word)
        res = set()
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(node: TrieNode, word: str, x: int, y: int):
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] == '#':
                return
            ch = board[x][y]
            if ch not in node.children:
                return
            word += ch
            child = node.children[ch]
            if word in words:
                res.add(word)
                # 剪枝叶，不然会超时
                if not child.children:
                    return
            board[x][y] = '#'
            for v in d:
                nx, ny = x+v[0], y+v[1]
                dfs(child, word, nx, ny)
            board[x][y] = ch
        for i in range(n):
            for j in range(m):
                dfs(trie.root, '', i, j)
        return list(res)