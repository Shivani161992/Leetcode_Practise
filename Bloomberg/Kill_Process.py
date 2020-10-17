from typing import List
pid =  [1, 3, 10, 5, 11, 2]
ppid = [3, 0, 5, 3, 5, 11]
kill = 5
from collections import Counter, defaultdict


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        kill_process = [kill]
        group_process = defaultdict(list)

        for child, parent in zip(pid, ppid):
            group_process[parent].append(child)

        for i in kill_process:
            kill_process.extend(group_process.get(i, []))

        return kill_process


obj=Solution()
print(obj.killProcess(pid, ppid, kill))
