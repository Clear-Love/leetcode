'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 21:43:59
LastEditors: lmio 2091319361@qq.com
Description: 
'''
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        def clone_node(node):
            if node in visited:
                return visited[node]
            clone = Node(node.val)
            visited[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(clone_node(neighbor))
            return clone
        return clone_node(node)