'''
Author: lmio 2091319361@qq.com
Date: 2023-07-08 14:56:17
LastEditors: lmio 2091319361@qq.com
Description: 61. 旋转链表
'''

from typing import Optional

from utils.node import ListNode

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None
    dummy = ListNode()
    dummy.next = head
    cur = head
    length = 0
    end = dummy
    while cur:
        if not cur.next:
            end = cur
        cur = cur.next
        length += 1
    cur = dummy
    print(length)
    k = k%length
    if k == 0:
        return head
    for _ in range(length-k):
        cur = cur.next
    l = cur.next
    cur.next = None
    end.next = head
    return l