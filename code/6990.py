'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 22:30:20
LastEditors: lmio 2091319361@qq.com
Description: 6990. 取整购买后的账户余额
'''

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        less = (purchaseAmount//10)*10
        more = less + 10
        
        return 100-less if abs(less-purchaseAmount) < abs(more-purchaseAmount) else 100-more