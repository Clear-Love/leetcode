'''
Author: lmio 2091319361@qq.com
Date: 2023-08-02 19:28:57
LastEditors: lmio 2091319361@qq.com
Description: 线段树
'''

from typing import List


class SegNode:
    def __init__(self):
        self.left = 0
        self.right = 0
        # 有多少个1
        self.sum = 0
        # 懒标记
        self.lazytag = False

class SegTree:
    def __init__(self, nums):
        n = len(nums)
        self.arr: List[SegNode] = [SegNode() for _ in range(n * 4 + 1)]
        self.build(0, 0, n - 1, nums)

    def sum_range(self, left, right):
        return self.query(0, left, right)

    def reverse_range(self, left, right):
        self.modify(0, left, right)

    def build(self, id, l, r, nums):
        arr = self.arr
        arr[id] = SegNode()
        arr[id].left = l
        arr[id].right = r
        arr[id].lazytag = False
        # 叶子结点
        if l == r:
            arr[id].sum = nums[l]
            return
        mid = (l + r) >> 1
        self.build(2 * id + 1, l, mid, nums)
        self.build(2 * id + 2, mid + 1, r, nums)
        arr[id].sum = arr[2 * id + 1].sum + arr[2 * id + 2].sum

    # pushdown函数：下传懒标记，即将当前区间的修改情况下传到其左右孩子结点，用到再修改
    def pushdown(self, x):
        arr = self.arr
        if arr[x].lazytag:
            arr[2 * x + 1].lazytag = not arr[2 * x + 1].lazytag
            arr[2 * x + 1].sum = arr[2 * x + 1].right - arr[2 * x + 1].left + 1 - arr[2 * x + 1].sum
            arr[2 * x + 2].lazytag = not arr[2 * x + 2].lazytag
            arr[2 * x + 2].sum = arr[2 * x + 2].right - arr[2 * x + 2].left + 1 - arr[2 * x + 2].sum
            arr[x].lazytag = False
    # 区间修改
    def modify(self, id, l, r):
        arr = self.arr
        # 子区间结点
        if arr[id].left >= l and arr[id].right <= r:
            # 反转
            arr[id].sum = (arr[id].right - arr[id].left + 1) - arr[id].sum
            arr[id].lazytag = not arr[id].lazytag
            return
        self.pushdown(id)
        if arr[2 * id + 1].right >= l:
            self.modify(2 * id + 1, l, r)
        if arr[2 * id + 2].left <= r:
            self.modify(2 * id + 2, l, r)
        arr[id].sum = arr[2 * id + 1].sum + arr[2 * id + 2].sum

    # 区间查询
    def query(self, id, l, r):
        arr = self.arr
        if arr[id].left >= l and arr[id].right <= r:
            return arr[id].sum
        if arr[id].right < l or arr[id].left > r:
            return 0
        self.pushdown(id)
        res = 0
        if arr[2 * id + 1].right >= l:
            res += self.query(2 * id + 1, l, r)
        if arr[2 * id + 2].left <= r:
            res += self.query(2 * id + 2, l, r)
        return res