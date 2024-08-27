'''
Author: lmio 2091319361@qq.com
Date: 2024-03-11 22:21:47
LastEditors: lmio 2091319361@qq.com
Description: 2129. 将标题首字母大写
'''

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        i = 0
        title = list(title)
        n = len(title)
        while i < n:
            word = []
            while i < n and title[i] != ' ':
                word.append(title[i])
                i += 1
            l = len(word)
            title[i-l+1] = title[i-l+1].upper()
            if l == 2:
                title[i-l+2] = title[i-l+2].upper()
            i += 1
        return str(title)
