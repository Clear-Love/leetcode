'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 17:22:05
LastEditors: lmio 2091319361@qq.com
Description: 345. 反转字符串中的元音字母
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        index = []
        s = list(s)
        for i, ch in enumerate(s):
            if ch in 'aAeEiIoOuU':
                index.append(i)
        i, j = 0, len(index)-1
        while i < j:
            s[index[i]], s[index[j]] = s[index[j]], s[index[i]]
            j -= 1
            i += 1
        return ''.join(s)
    