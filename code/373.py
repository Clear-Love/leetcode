'''
Author: lmio 2091319361@qq.com
Date: 2023-07-15 15:43:52
LastEditors: lmio 2091319361@qq.com
Description: 
'''
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 判断 nums1 和 nums2 的长度，将较短的作为 nums1
        flag, ans = (n := len(nums1)) > (m := len(nums2)), []
        if flag:
            n, m, nums1, nums2 = m, n, nums2, nums1
        # 创建一个空的优先队列
        pq = []
        # 将 nums1 和 nums2 的前 n 个元素的和以及对应的索引添加到优先队列中
        for i in range(min(n, k)):
            heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))
        # 当结果列表的长度小于 k 且优先队列不为空时，继续循环
        while len(ans) < k and pq:
            # 弹出优先队列中和最小的元素及其索引
            _, a, b = heapq.heappop(pq)
            # 将数字对添加到结果列表中，根据 flag 判断 nums1 和 nums2 的顺序
            ans.append([nums2[b], nums1[a]] if flag else [nums1[a], nums2[b]])
            # 如果 nums2 还有下一个元素，则将下一个元素和 nums1[a] 的和及索引添加到优先队列中
            if b + 1 < m:
                heapq.heappush(pq, (nums1[a] + nums2[b + 1], a, b + 1))
        return ans