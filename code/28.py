'''
Author: lmio 2091319361@qq.com
Date: 2023-07-02 23:09:30
LastEditors: lmio 2091319361@qq.com
Description: 28. 找出字符串中第一个匹配项的下标
'''

# KMP算法

def strStr(haystack: str, needle: str) -> int:
    n = len(needle)
    m = len(haystack)
    #构造next数组
    next = [0]
    k = 0
    for i in range(1, n):
        while k > 0 and needle[k] != needle[i]:
            k = next[k-1];
        if needle[k] == needle[i]:
            k += 1
        next.append(k)
    k = 0
    for i in range(m):
        while k > 0 and haystack[i] != needle[k]:
            k = next[k-1]
        if haystack[i] == needle[k]:
            k += 1
        if k == n:
            return i-k+1
    return -1