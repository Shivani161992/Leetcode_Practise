from typing import List
intervals = [[1,4],[2,3]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        if len(intervals)==1:
            return intervals
        merge=[]
        hold=intervals[0]
        for i in range(1, len(intervals)):
            interv=intervals[i]
            if interv[0] <= hold[1]:
                hold[1]=max(interv[1], hold[1])
                if hold not in merge:
                    merge.append(hold)
            elif interv[0] > hold[1]:
                if hold not in merge:
                    merge.append(hold)
                if len(intervals)-1 == i:
                    merge.append(interv)
                hold=interv
        return merge






obj=Solution()
print(obj.merge(intervals))