'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 18:05:19
LastEditors: lmio 2091319361@qq.com
Description: 443. 压缩字符串
'''
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        wp = 0
        while i < len(chars):
            cnt = 1
            ch = chars[i]
            chars[wp] = ch
            wp += 1
            i += 1
            while i < len(chars) and chars[i] == ch:
                cnt += 1
                i += 1
            if cnt > 1:
                for v in str(cnt):
                    chars[wp] = v
                    wp += 1
        print(chars)
        return wp