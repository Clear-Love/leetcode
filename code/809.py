'''
Author: lmio 2091319361@qq.com
Date: 2023-07-24 23:38:19
LastEditors: lmio 2091319361@qq.com
Description: 809. 情感丰富的文字
'''

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word: str) -> bool:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False
                count_s = 1
                count_word = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count_s += 1
                    i += 1
                while j + 1 < len(word) and word[j] == word[j + 1]:
                    count_word += 1
                    j += 1
                if count_s < count_word or (count_s > count_word and count_s < 3):
                    return False
                i += 1
                j += 1
            return i == len(s) and j == len(word)

        count = 0
        for word in words:
            if is_stretchy(word):
                count += 1
        return count
