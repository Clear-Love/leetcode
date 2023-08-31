'''
Author: lmio 2091319361@qq.com
Date: 2023-08-28 19:43:06
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.22. 单词转换
'''

from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        word_dic = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                word_dic[word[:i] + '*' + word[i+1:]].add(word)
        res = []
        path = [beginWord]
        visited = set()
        visited.add(beginWord)
        def dfs(cur: str):
            nonlocal res
            if cur == endWord:
                res = path
                return
            for i in range(len(cur)):
                for word in word_dic[cur[:i] + '*' + cur[i+1:]]:
                    if word not in visited:
                        visited.add(word)
                        path.append(word)
                        dfs(word)
                        if res:
                            return
                        path.pop()
                        visited.remove(word)
        dfs(beginWord)
        return res