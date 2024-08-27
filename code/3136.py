'''
Author: lmio 2091319361@qq.com
Date: 2024-05-06 15:53:02
LastEditors: lmio 2091319361@qq.com
Description: 3136. 有效单词
'''

class Solution:
    def isValid(self, word: str) -> bool:
        m = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        if len(word) < 3:
            return False
        f1, f2 = False, False
        for w in word:
            if not w.isalnum():
                return False
            if not f1 and w in m:
                f1 = True
            if not f2 and w.isalpha() and w not in m:
                f2 = True
        return f1 and f2
            