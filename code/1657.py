'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 22:10:57
LastEditors: lmio 2091319361@qq.com
Description:1657. 确定两个字符串是否接近 
'''

from collections import Counter, defaultdict



class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 出现次数, 不同字母个数
        c1=Counter(word1)
        c2=Counter(word2)
        l1=sorted(c1.values())
        l2=sorted(c2.values())
        l3=sorted(c1.keys())
        l4=sorted(c2.keys())
        return l1==l2 and l3==l4