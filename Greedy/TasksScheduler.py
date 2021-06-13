from typing import List
from collections import Counter
tasks= ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n=2
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        else:
            tasksCollection = dict(Counter(tasks))  # {A= 5, B=0, C=0, D= 1, E=1,F=1, G=1}
            minTime = 0  # 1 2
            prev = ""
            seen = set()  # B-C
            while len(seen) != len(tasksCollection):
                taskLeft = -1  # 0 1 2
                hold = ""  # ABC
                for task in tasksCollection:
                    if task not in seen:
                        hold = hold + task
                        tasksCollection[task] = tasksCollection[task] - 1
                        if tasksCollection[task] == 0:
                            seen.add(task)
                        taskLeft = taskLeft + 1
                        minTime = minTime + 1
                        if taskLeft == n:
                            break
                        else:
                            continue

                if len(seen) == len(tasksCollection):
                    break
                if taskLeft != n and hold == prev:
                    minTime = minTime + (n - taskLeft)
                prev = hold

            return minTime

obj=Solution()
print(obj.leastInterval(tasks, n))






