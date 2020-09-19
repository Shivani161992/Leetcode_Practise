from typing import List
intervals= [[6,10],[13,14],[12,14]]
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0:
            return 0
        else:
            intervals.sort(key= lambda x : x[0])
            end = intervals[0][1]

obj=Solution()
print(obj.minMeetingRooms(intervals))

