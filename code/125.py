'''
Author: lmio 2091319361@qq.com
Date: 2023-07-04 16:17:29
LastEditors: lmio 2091319361@qq.com
Description: 125. 验证回文串
'''
import re


def isPalindrome(s: str) -> bool:
    # 将字符串中的大写字符转换为小写
    s =  s.lower()
    # 使用正则表达式去除非数字字母字符
    s = re.sub('[^a-z0-9]', '', s)
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True