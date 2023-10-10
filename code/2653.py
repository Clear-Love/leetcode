'''
Author: lmio 2091319361@qq.com
Date: 2023-09-30 18:09:20
LastEditors: lmio 2091319361@qq.com
Description: 2653. 滑动子数组的美丽值
'''

from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = [0] * 101
        for num in nums[:k-1]:  # 先往窗口内添加 k-1 个数
            cnt[num] += 1
        res = [0] * (len(nums) - k + 1)
        n = len(nums)
        left, right = 0, k-1
        while right < n:
            cnt[nums[right]] += 1
            r = x
            for i in range(-50, 0):
                if cnt[i]:
                    r -= cnt[i]
                    if r <= 0:
                        res[left] = i
                        break
            cnt[nums[left]] -= 1
            right += 1
            left += 1
        return res