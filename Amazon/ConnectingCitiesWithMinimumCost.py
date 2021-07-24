from typing import List
from collections import defaultdict

n = 7
connections = [[2,1,87129],[3,1,14707],[4,2,34505],[5,1,71766],[6,5,2615],[7,2,37352]]

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) == 1:
            return connections[0][2]
        else:
            minCost = 0
            visited = []
            connected=0
            adjList = defaultdict(list)
            connections.sort(key=lambda x: x[2])
            for con in connections:
                city1 = con[0]
                city2 = con[1]
                if (city1 not in visited or city2 not in visited):
                    minCost= minCost + con[2]
                    visited.append(city1)
                    visited.append(city2)
                    adjList[city1].append(city2)
                    adjList[city2].append(city1)

            visitedcity=set()
            for i in range(1, n+1):
                if i not in visitedcity:
                    connected = connected + 1
                    if i in adjList:
                        self.dfs(i, visitedcity, adjList)
                if connected > 1:
                    return -1
            return minCost

    def dfs(self, i, visitedcity, adjList):
        if i in adjList:
            getConnectedNodes= adjList[i]
            visitedcity.add(i)
            for node in getConnectedNodes:
                if node not in visitedcity:
                    self.dfs(node, visitedcity, adjList)






obj = Solution()
print(obj.minimumCost(n, connections))
