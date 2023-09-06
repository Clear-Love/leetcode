'''
Author: lmio 2091319361@qq.com
Date: 2023-09-01 16:30:29
LastEditors: lmio 2091319361@qq.com
Description: 707. 设计链表
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

class MyLinkedList:

    def __init__(self):
        self.head: ListNode = ListNode()
        self.tail: ListNode = self.head
        self.size: int = 0

    def get(self, index: int) -> int:
        node = self.head
        if index < 0 or index >= self.size:
            return -1
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head)
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.tail.val = val
        self.tail.next = ListNode()
        self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        pre = ListNode(next=self.head)
        cur = self.head
        for _ in range(index):
            pre = pre.next
            cur = cur.next
        pre.next = ListNode(val, cur)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.size == 0:
            return
        cur = self.head
        if index == 0:
            self.head = cur.next
            self.size -= 1
            return
        if index >= self.size:
            return
        for _ in range(index-1):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
