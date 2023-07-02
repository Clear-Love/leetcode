'''
Author: lmio 2091319361@qq.com
Date: 2023-07-02 22:48:02
LastEditors: lmio 2091319361@qq.com
Description: 151. 反转字符串中的单词
'''

def reverseWords(s: str) -> str:
    s = s.strip()
    res = []
    i = len(s)-1
    while i > 0:
        j = i
        while j > 0 and s[j] != ' ':
            j -= 1
        res.append(s[j+1:i+1])
        while j > 0 and s[j] == ' ':
            j -= 1
        i = j
    return ' '.join(res)