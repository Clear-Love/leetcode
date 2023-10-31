'''
Author: lmio 2091319361@qq.com
Date: 2023-10-24 22:41:36
LastEditors: lmio 2091319361@qq.com
Description: 132. 分割回文串 II
'''

class Solution:
    def minCut(self, s: str) -> int:
        def is_pal(t: str) -> int:
            