from typing import List
from collections import defaultdict

numCourses = 7
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) != 0:
            connections= defaultdict(list)
            for pre in prerequisites:
                connections[pre[0]].append(pre[1])
            visited=[]
            for courses in range(0, numCourses):
                if courses not in visited:
                    stack=[courses]
                    while stack:
                        getNode= stack[-1]
                        if getNode in connections:
                            getConnection= connections[getNode]
                            count=0
                            for con in getConnection:
                                count = count +1
                                if con not in visited:
                                    if con not in stack:
                                        stack.append(con)
                                        break

                        elif getNode not in connections:
                            stack.pop()
                            visited.append(getNode)
            return True






    def dfs(self, connections, stack, visited, complete):
        while stack:
            node= stack[-1]
            if node in connections:
                getConnections= connections[node]
                for con in getConnections:
                    if con not in visited:
                        if con not in stack:
                            stack.append(con)
                            result=self.dfs(connections, stack, visited, complete)
                            return False if result == False else True
                        else:
                            return False
            stack.pop()
            visited.append(node)





obj=Solution()
print(obj.canFinish(numCourses, prerequisites))

