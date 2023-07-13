'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 21:48:47
LastEditors: lmio 2091319361@qq.com
Description: 399. 除法求值
'''
from collections import defaultdict, namedtuple
from typing import List



def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    Node = namedtuple('Node', ['label', 'value'])
    graph = defaultdict(list)
    for i, edge in enumerate(equations):
        n1, n2 = edge
        val = values[i]
        graph[n1].append(Node(n2, val))
        graph[n2].append(Node(n1, 1/val))
    def bfs(start: str, end: str) -> float:
        if start not in graph:
            return -1.0
        visited = set()  # 用于记录已访问的节点
        queue = [Node(start, 1)] # 使用队列进行广度优先搜索，同时记录路径
        while queue:
            node = queue[0]
            queue = queue[1:]
            label = node.label
            val = node.value
            visited.add(label)
            if label == end:
                return val  # 找到目标节点，返回结果
            for neighbor in graph[label]:
                if neighbor.label not in visited:
                    queue.append(Node(neighbor.label, neighbor.value*val))  # 将邻居节点添加到队列，并记录值
        return -1.0  # 未找到路径
    res = []
    for v in queries:
        res.append(bfs(v[0], v[1]))
    return res

print(calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))