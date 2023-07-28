'''
Author: lmio 2091319361@qq.com
Date: 2023-07-28 21:27:52
LastEditors: lmio 2091319361@qq.com
Description:2130. 链表最大孪生和 
'''
from typing import Optional

from utils.node import ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        l, r = 0, len(arr)-1
        res = float('-inf')
        while l < r:
            res = max(res, arr[l]+arr[r])
            l += 1
            r -= 1
        return res