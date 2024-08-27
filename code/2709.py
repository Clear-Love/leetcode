'''
Author: lmio 2091319361@qq.com
Date: 2024-05-15 20:35:10
LastEditors: lmio 2091319361@qq.com
Description: 2709. 最大公约数遍历
'''

from typing import Counter, List


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # 并查集
        MX = max(nums) + 1
        fa = list(range(MX))
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        # 分解质因数
        def sqrt(n: int) -> List[int]:
            res = []
            i = 2
            while i * i <= n:
                i2 = i * i
                flag = False
                while n % i2 == 0:
                    if not flag:
                        res.append(i)
                        flag = True
                    n //= i2
                if n % i == 0:
                    if not flag:
                        res.append(i)
                    n //= i
                i += 1
            if n > 1:
                res.append(n)
            return res
        
        cnt = Counter()
        for i,el in enumerate(nums):
            cur = sqrt(el)
            fx = find(el)
            for x in cur:
                if x in cnt.keys():
                    index = cnt[x]
                    fy = find(nums[index])
                    if fx == fy:continue
                    fa[fy] = fx 
                cnt[x] = i 
        st = set()
        cnt1 = 0
        for el in nums:
            if el == 1:
                cnt1 += 1
            else:
                st.add(find(el))
        return len(st) + cnt1 < 2