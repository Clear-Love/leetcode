'''
Author: lmio 2091319361@qq.com
Date: 2024-03-31 16:51:19
LastEditors: lmio 2091319361@qq.com
Description: 331. 验证二叉树的前序序列化
'''

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        diff = 1
        for node in preorder.split(','):
            # 减去入度
            diff -= 1
            if diff < 0:
                return False
            # 非叶子节点加上出度
            if node != '#':
                diff += 2
        return not diff