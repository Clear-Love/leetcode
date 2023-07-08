'''
Author: lmio 2091319361@qq.com
Date: 2023-07-08 16:47:11
LastEditors: lmio 2091319361@qq.com
Description: 146. LRU 缓存
'''

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        # 移动到表尾部
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # 删除最久未使用的元素（表头元素）
            self.cache.popitem(last=False)
        self.cache[key] = value
