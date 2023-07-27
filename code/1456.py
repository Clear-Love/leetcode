'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 20:52:55
LastEditors: lmio 2091319361@qq.com
Description: 1456. 定长子串中元音的最大数目
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(ch: str):
            return ch in 'aeiou'
        cnt = 0
        left, right = 1, k
        for i in range(k):
            if isVowel(s[i]):
                cnt += 1
        res = cnt
        while right < len(s):
            if isVowel(s[left-1]):
                cnt -= 1
            if isVowel(s[right]):
                cnt += 1
            res = max(res, cnt)
            left += 1
            right += 1
        return res
            