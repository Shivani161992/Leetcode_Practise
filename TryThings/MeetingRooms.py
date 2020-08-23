from typing import List
intervals= [[0, 30],[5, 10],[15, 20]]
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        else:
            intervals.sort(key=lambda x: x[0])
            end = intervals [0][1]
            for i in range(1, len(intervals)):
                new_end= intervals [i][1]
                if intervals[i][0] < end:
                    return False
                else:
                    end = new_end
            return True


Obj=Solution()
print(Obj.canAttendMeetings(intervals))

