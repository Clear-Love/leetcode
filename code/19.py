'''
Author: lmio 2091319361@qq.com
Date: 2023-07-08 11:05:40
LastEditors: lmio 2091319361@qq.com
Description: 19. 删除链表的倒数第 N 个结点
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    cur = head
    for _ in range(n):
        cur = cur.next
    while cur:
        cur = cur.next
        prev = prev.next
    prev.next = prev.next.next
    return dummy.next