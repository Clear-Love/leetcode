'''
Author: lmio 2091319361@qq.com
Date: 2024-04-11 19:12:50
LastEditors: lmio 2091319361@qq.com
Description: 门牌制作
'''

from typing import Counter

res = 0
for i in range(1, 2021):
    cnts = Counter(str(i))
    res += cnts['2']
print(res)