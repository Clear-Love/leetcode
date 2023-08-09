'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 22:27:20
LastEditors: lmio 2091319361@qq.com
Description: 面试题 10.03. 搜索旋转数组
'''

from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) >> 1
            if arr[left] < arr[mid]:
                # 目标值在左侧有序列表中
                if arr[left] <= target <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif arr[left] > arr[mid]:
                # 目标值在左侧
                if target >= arr[left] or target <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if arr[left] == target:
                    return left
                else:
                    left += 1
        return -1