'''
Author: lmio 2091319361@qq.com
Date: 2023-07-07 19:58:48
LastEditors: lmio 2091319361@qq.com
Description: 92. 反转链表 II
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    cur = prev.next
    # 不断把next插入到prev后面
    for _ in range(right - left):
        next = cur.next
        cur.next = next.next
        next.next = prev.next
        prev.next = next
    return dummy.next