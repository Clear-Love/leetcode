from typing import List


def removeDuplicates(nums: List[int]) -> int:
    left, right = 0, 1
    if len(nums) < 2:
        return 2
    while right < len(nums):
        if nums[left] == nums[right]:
            right += 1
            while right < len(nums) and nums[left] == nums[right]:
                nums.pop(right)
            left += 1
        left += 1
        right += 1
    return len(nums)

print(removeDuplicates([0,0,1,1,1,1,2,3,3]))