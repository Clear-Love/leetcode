'''
Author: lmio 2091319361@qq.com
Date: 2023-07-14 00:32:47
LastEditors: lmio 2091319361@qq.com
Description: 127. 单词接龙
'''
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque()
        def isNext(word: str, target: str):
            diff = 0
            for i in range(len(word)):
                if word[i] != target[i]:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1
        queue.append([beginWord, 1])
        while queue:
            tmp, step = queue.popleft()
            if tmp == endWord:
                return step
            toRemove = []
            for word in wordList:
                if isNext(tmp, word):
                    queue.append([word, step+1])
                    toRemove.append(word)
            for word in toRemove:
                wordList.remove(word)
        return 0