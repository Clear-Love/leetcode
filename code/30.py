'''
Author: lmio 2091319361@qq.com
Date: 2023-07-04 16:58:48
LastEditors: lmio 2091319361@qq.com
Description: 30. 串联所有单词的子串
'''

from collections import Counter
from typing import List

def findSubstring(s: str, words: List[str]) -> List[int]:
    if not s or not words:return []
    word_sz = len(words[0])
    word_num = len(words)
    words = Counter(words)
    res = []
    for i in range(0, word_sz):
        count = 0
        left = i
        right = i
        cur_Counter = Counter()
        while right + word_sz <= len(s):
            w = s[right:right + word_sz]
            right += word_sz
            cur_Counter[w] += 1
            count += 1
            # 单词出现次数太多，滑动窗口左边界移动到第一个重复单词右边
            while cur_Counter[w] > words[w]:
                left_w = s[left:left+word_sz]
                left += word_sz
                cur_Counter[left_w] -= 1
                count -= 1
            if count == word_num :
                res.append(left)
    return res