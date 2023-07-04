'''
Author: lmio 2091319361@qq.com
Date: 2023-07-04 20:57:26
LastEditors: lmio 2091319361@qq.com
Description: 76. 最小覆盖子串
'''

from collections import Counter


def minWindow(s: str, t: str) -> str:
    tCnt = Counter(t)
    cur_tCnt = Counter()
    left, right = 0, 0
    length = 0
    right = left
    res = (0, float('inf'))
    while right < len(s):
        while left < len(s) and s[left] not in tCnt:
            left += 1
        while right < len(s) and s[right] not in tCnt:
            right += 1
        if right >= len(s):
            break
        if s[right] in tCnt:
            cur_tCnt[s[right]] += 1
        if cur_tCnt[s[right]] <= tCnt[s[right]]:
            length += 1
        while length == len(t):
            if right - left < res[1] - res[0]:
                res=(left, right+1)
            cur_tCnt[s[left]] -= 1
            if cur_tCnt[s[left]] < tCnt[s[left]]:
                length -= 1
            left += 1
            while left < len(s) and s[left] not in tCnt:
                left += 1
        right += 1
    return "" if res[1] > len(s) else s[res[0]: res[1]]

print(minWindow("ADOBECODEBANC", "ABC"))