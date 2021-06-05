from typing import List
from collections import defaultdict
n = 2
edges = [[1,0]]
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        collection = defaultdict(set)
        for edge in edges:
            collection[edge[0]].add(edge[1])
        for i in range(0, n):
            if i not in visited:
                if i in collection:
                    stack = [i]
                    visited.add(i)
                    while stack:
                        getNode = stack.pop()
                        if getNode in collection:
                            getchild = collection[getNode]
                            for child in getchild:
                                if child not in visited:
                                    stack.append(child)
                                    visited.add(child)
                                else:
                                    return False

                else:
                    visited.add(i)
            if len(visited) != n:
                return False
            else:
                return True
        return True


obj=Solution()
print(obj.validTree(n, edges))