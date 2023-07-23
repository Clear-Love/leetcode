from collections import defaultdict
from typing import List


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = defaultdict(list)
        for i in range(1, n):
            graph[parent[i]].append(i)
            graph[i].append(parent[i])

        count = [0]
        self.dfs(graph, s, 0, -1, count, [0] * 26)
        return count[0]

    def dfs(self, graph, s, node, parent, count, char_count):
        char_count[ord(s[node]) - ord('a')] += 1
        for child in graph[node]:
            if child != parent:
                self.dfs(graph, s, child, node, count, char_count)

        count[0] += sum(v % 2 == 1 for v in char_count)
        count[0] -= int(s[node] != '#')
        char_count[ord(s[node]) - ord('a')] -= 1