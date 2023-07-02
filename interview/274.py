from typing import List


def hIndex(citations: List[int]) -> int:
    citations.sort(reverse=True)
    right = 0
    while right < len(citations):
        right += 1
        if right > citations[right-1]:
            right -= 1
            break
    return right

print(hIndex([3, 0, 6, 1, 5]))