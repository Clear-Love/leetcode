'''
Author: lmio 2091319361@qq.com
Date: 2023-07-08 10:20:31
LastEditors: lmio 2091319361@qq.com
Description: 25. K 个一组翻转链表
'''

from typing import Optional

from utils.node import ListNode


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverse(node: ListNode, k: int) -> ListNode:
        prev = node
        if not node.next:
            return None
        cur = prev.next
        # 不断把next插入到prev后面
        i = 1
        while i < k:
            if not cur.next:
                return reverse(prev, i)
            next = cur.next
            cur.next = next.next
            next.next = prev.next
            prev.next = next
            i += 1
        return cur
    node = ListNode()
    node.next = head
    dummy = node
    while node:
        node = reverse(node, k)
    return dummy.next