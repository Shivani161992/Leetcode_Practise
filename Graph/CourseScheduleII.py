from typing import List
from collections import defaultdict    

numCourses = 3
prerequisites = [[0, 1], [0, 2], [1, 2]]
class Solution:
    def findOrder1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [i for i in range(numCourses - 1, -1, -1)]
        else:
            order = []
            courses = defaultdict(list)
            for p in prerequisites:
                courses[p[0]].append(p[1])

            seen = []
            for c in range(numCourses):
                stack = [c]
                while len(stack) != 0:
                    getCour = stack[-1]
                    if getCour in courses and courses[getCour] != None:
                        getChild = courses[getCour]
                        courses[getCour] = None
                        for i in range(len(getChild) - 1, -1, -1):
                            if getChild[i]  in stack: 
                                return []
                            elif getChild[i]  not in stack:
                                if getChild[i] not in seen:
                                    stack.append(getChild[i])
                    else:
                        order.append(getCour)
                        stack.pop()
                        seen.append(getCour)

            return order

    def findOrder(self, numCourses, prerequisites):
        self.graph = defaultdict(list)  # a graph for all courses
        self.res = []  # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1])
            self.visited = [0 for x in range(numCourses)]  # DAG detection
        for x in range(numCourses):
            if not self.DFS(x):
                return []
            # continue to search the whole graph
        return self.res

    def DFS(self, node):
        if self.visited[node] == -1:  # cycle detected
            return False
        if self.visited[node] == 1:
            return True  # has been finished, and been added to self.res
        self.visited[node] = -1  # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1  # mark as finished
        self.res.append(node)  # add to solution as the course depenedent on previous ones
        return True


obj = Solution()
print(obj.findOrder1(numCourses, prerequisites))
