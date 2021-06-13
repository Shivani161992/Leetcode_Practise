from typing import List
from collections import defaultdict

n = 4
edges = [[0,1],[2,3],[1,2]]


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        elif n == 1:
            return True
        else:
            validTree=False
            visited = []
            parent = -1
            connections = defaultdict(list)
            for edge in edges:
                connections[edge[0]].append(edge[1])
                connections[edge[1]].append(edge[0])

            for i in range(0, n):
                if i not in visited:
                    if i in connections:
                        stack = [i]
                        validTree = self.dfs(connections, visited, stack, parent)
                        if validTree == False:
                            return validTree

                if len(visited) !=n:
                    return False
            return validTree


    def dfs(self, connections, visited, stack, parent):
        valid = None
        oriparent=parent
        while stack:
            getNode = stack.pop()
            visited.append(getNode)
            if getNode in connections:
                getChildrens = connections[getNode]
                for child in getChildrens:
                    parent= oriparent
                    if child not in visited:
                        stack.append(child)
                        parent = getNode
                        valid = self.dfs(connections, visited, stack, parent)
                        if valid == False:
                            return False
                    elif child in visited:
                        if child != parent:
                            return False
                return False if valid==False else True

        return False if valid == False else True


obj = Solution()
print(obj.validTree(n, edges))
