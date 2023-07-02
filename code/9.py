'''
Author: lmio 2091319361@qq.com
Date: 2023-06-26 15:50:05
LastEditors: lmio 2091319361@qq.com
Description: 8. 字符串转换整数 (atoi)
'''
def myAtoi(s: str) -> int:
    # 去除前导空格
    s = s.lstrip()
    if not s:
        return 0

    # 判断正负号
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    
    sum = 0
    for ch in s:
        if not ch.isdigit():
            break
        sum = sum*10+int(ch)
    return sign*sum
