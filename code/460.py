'''
Author: lmio 2091319361@qq.com
Date: 2023-09-25 17:16:52
LastEditors: lmio 2091319361@qq.com
Description: 460. LFU 缓存
'''

from collections import defaultdict
from typing import Optional, OrderedDict

class Node:
    def __init__(self, value: int) -> None:
        self.freq = 1
        self.val = value

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_to_node = {}
        self.min_freq = 0
        self.freq_to_dict = defaultdict(OrderedDict)

    def get_node(self, key: int) -> Optional[bool]:
        # 没找到
        if key not in self.key_to_node:
            return False
        node = self.key_to_node[key]
        del self.freq_to_dict[node.freq][key]
        if not self.freq_to_dict[node.freq]:
            del self.freq_to_dict[node.freq]
            if node.freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1
        self.freq_to_dict[node.freq][key] = node
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.val = value  # 更新 value
            return
        if len(self.key_to_node) == self.cap:
            k, node = self.freq_to_dict[self.min_freq].popitem(last=False)
            del self.key_to_node[k]
            if not self.freq_to_dict[node.freq]:
                del self.freq_to_dict[node.freq]
        node = Node(value)
        self.key_to_node[key] = node
        self.freq_to_dict[1][key] = node
        self.min_freq = 1