from typing import List
intervals= [[6,10],[13,14],[12,14]]
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0:
            return 0
        else:
            intervals.sort(key=lambda x: x[0])
            end= intervals[0][1]
            rooms=1
            seen=[]
            for i in range(1, len(intervals)):
                new_start = intervals[i][0]
                new_end = intervals[i][1]
                if intervals[i] in seen:
                    rooms= rooms + 1
                else:
                    seen.append(intervals[i])
                    if new_start < end:
                        rooms= rooms + 1
                        if end > new_end:
                            end = new_end
            return rooms

obj=Solution()
print(obj.minMeetingRooms(intervals))

