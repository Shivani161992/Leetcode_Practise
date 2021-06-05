from typing import List
from collections import defaultdict

n = 10
edges = [[5,8],[3,5],[1,9],[4,5],[0,2],[7,8],[4,9]]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        else:
            visited = set()
            count = 0
            connections = defaultdict(set)
            for edge in edges:
                connections[edge[0]].add(edge[1])
                connections[edge[1]].add(edge[0])

            for i in range(0, n):
                if i not in visited:
                    count = count + 1
                    if i in connections:
                        stack=[i]
                        while stack:
                            node = stack.pop()
                            visited.add(node)
                            child= connections[node]
                            for c in child:
                                if c not in visited:
                                    stack.append(c)
            return count




obj = Solution()
print(obj.countComponents(n, edges))
