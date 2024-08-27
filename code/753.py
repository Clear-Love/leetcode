'''
Author: lmio 2091319361@qq.com
Date: 2024-05-27 20:07:05
LastEditors: lmio 2091319361@qq.com
Description: 753. 破解保险箱
'''

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        vis = set()
        res = list()
        # 假设当前按了n-位0
        highest = 10 ** (n - 1)
        def dfs(node: int):
            for x in range(k):
                # 按下x
                nei = node * 10 + x
                if nei not in vis:
                    vis.add(nei)
                    # 取倒数n位
                    dfs(nei % highest)
                    res.append(str(x))
        dfs(0)
        # 算法res按钮顺序是倒着的，所以0添加到字符末尾
        return "".join(res) + "0" * (n - 1)