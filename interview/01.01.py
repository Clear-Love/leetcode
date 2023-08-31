'''
Author: lmio 2091319361@qq.com
Date: 2023-08-31 19:25:52
LastEditors: lmio 2091319361@qq.com
Description: 面试题 01.01. 判定字符是否唯一
'''

class Solution:
    def isUnique(self, astr: str) -> bool:
        vis = [False]*26
        for ch in astr:
            key = ord(ch) - ord('a')
            if vis[key]:
                return False
            vis[key] = True
        return True