from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        S = sorted(S)
        res = []
        path = []
        visited = [False]*n
        def dfs():
            if len(path) == n:
                res.append(''.join(path))
                return
            for i in range(n):
                # 去重
                if i > 0 and S[i] == S[i-1] and visited[i-1]:
                    continue
                ch = S[i]
                if not visited[i]:
                    visited[i] = True
                    path.append(ch)
                    dfs()
                    path.pop()
                    visited[i] = False
        dfs()
        return res