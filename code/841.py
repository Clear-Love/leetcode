'''
Author: lmio 2091319361@qq.com
Date: 2023-07-29 21:27:34
LastEditors: lmio 2091319361@qq.com
Description: 841. 钥匙和房间
'''

from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        q = deque()
        q.append(0)
        while q:
            room = q.popleft()
            visited.add(room)
            for v in rooms[room]:
                if v not in visited:
                    q.append(v)
        return len(visited) == n