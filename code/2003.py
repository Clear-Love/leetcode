'''
Author: lmio 2091319361@qq.com
Date: 2023-10-31 23:32:09
LastEditors: lmio 2091319361@qq.com
Description: 2003. 每棵子树内缺失的最小基因值
'''

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        res = [1] * n
        if 1 not in nums:
            return res
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parents[i]].append(i)
        vis = set()
        def dfs(x: int) -> None:
            vis.add(nums[x])
            for son in g[x]:
                if nums[son] not in vis:
                    dfs(son)
        mv = 2
        node = nums.index(1)
        while node >= 0:
            dfs(node)
            while mv in vis:
                mv += 1
            res[node] = mv
            node = parents[node]
        return res