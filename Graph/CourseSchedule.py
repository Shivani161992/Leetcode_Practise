from collections import defaultdict
from typing import List

numCourses = 7
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        if len(prerequisites) == 0 and numCourses != 0:
            return True
        else:
            courses = defaultdict(list)
            for p in prerequisites:
                courses[p[0]].append(p[1])

            traverse = []
            canTake = []
            stack = []
            for c in courses:
                if c not in traverse:
                    stack.append(c)
                    while len(stack) != 0:
                        getCourse = stack[-1]
                        if getCourse in courses:
                            getPreq = courses[getCourse]
                            all = True

                            for pq in range(len(getPreq) - 1, -1, -1):
                                if getPreq[pq] not in traverse:
                                    all = False
                                    if getPreq[pq] not in stack:
                                        stack.append(getPreq[pq])
                                    elif getPreq[pq] in stack:
                                        if getPreq[pq] not in courses:
                                            canTake.append(getCourse)
                                        traverse.append(getPreq[pq])
                            if all == True:
                                stack.pop()
                                if getCourse not in traverse:
                                    traverse.append(getCourse)
                                children = len(getPreq)
                                count = 0
                                for pq in range(len(getPreq) - 1, -1, -1):
                                    if getPreq[pq] in canTake:
                                        count = count + 1
                                if count == children:
                                    canTake.append(getCourse)

                        elif getCourse not in courses:
                            stack.pop()
                            canTake.append(getCourse)
                            traverse.append(getCourse)
            print(canTake)
            return True if ((len(canTake) >= numCourses) or len(canTake) == len(traverse)) else False


obj = Solution()
print(obj.canFinish(numCourses, prerequisites))
