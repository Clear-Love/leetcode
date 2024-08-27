'''
Author: lmio 2091319361@qq.com
Date: 2024-04-10 20:08:40
LastEditors: lmio 2091319361@qq.com
Description: 1702. 修改后的最大二进制字符串
'''

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        i = binary.find('0')
        if i < 0:
            return binary
        cnt1 = binary.count('1', i)
        return '1' * (len(binary) - 1 - cnt1) + '0' + '1' * cnt1