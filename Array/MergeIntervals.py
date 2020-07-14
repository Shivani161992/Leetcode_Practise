from typing import List
intervals=[[1,4], [4,5], [0,1]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return intervals
        addList=[]
        hold=''
        intervals=sorted(intervals, key=lambda x : x[0])
        for i, v in enumerate(intervals):
            if (i==0):
                hold=v
            else:
                if(hold[1]>=v[0]):
                    hold=[hold[0], v[1]]
                elif (hold[1]<v[0]):
                    addList.append(hold)
                    hold=v
        addList.append(hold)
        return addList


o=Solution()
y=o.merge(intervals)
print(y)