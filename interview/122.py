from typing import List

def maxProfit(self, prices: List[int]) -> int:
    left, right = 0, 1
    res = 0
    while right < len(prices):
        if prices[right] > prices[left]:
            res += prices[right] - prices[left]
        left += 1
        right += 1
    return res