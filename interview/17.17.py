'''
Author: lmio 2091319361@qq.com
Date: 2023-08-24 22:47:09
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.17. 多次搜索
'''
from typing import List

from utils.trie import Trie


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in smalls:
            trie.insert(word)
        res = [[] for _ in range(len(smalls))]
        pos = {v: i for i, v in enumerate(smalls)}
        for i in range(len(big)):
            node = trie.root
            j = i
            while j < len(big) and big[j] in node.children:
                node = node.children[big[j]] 
                if node.is_word:
                    res[pos[big[i:j+1]]].append(i)
                j += 1
        return res