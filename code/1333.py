'''
Author: lmio 2091319361@qq.com
Date: 2023-09-27 18:24:34
LastEditors: lmio 2091319361@qq.com
Description: 1333. 餐厅过滤器
'''

from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        veganFriendly = 0 if veganFriendly else 1
        return [rest[0] for rest in sorted([rest for rest in restaurants if veganFriendly|rest[2] and rest[3] <= maxPrice and rest[4] <= maxDistance], key=lambda x: (x[1], x[0]), reverse=True)]