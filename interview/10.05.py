'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 23:24:36
LastEditors: lmio 2091319361@qq.com
Description: 面试题 10.05. 稀疏数组搜索
'''

from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left, right = 0, len(words) - 1
        while left <= right:
            mid = (right + left) >> 1
            temp = mid
            while words[mid] == '' and mid < right:
                mid += 1
            if words[mid] == '':  
                right = temp - 1
                continue
            if words[mid] == s:
                return mid
            elif s < words[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1