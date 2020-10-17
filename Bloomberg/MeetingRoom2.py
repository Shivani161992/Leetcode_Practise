from typing import List
intervals= [[0, 30],[5, 10],[15, 20]]
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        else:
            intervals.sort(key=lambda x:x[0])
            end_times=[intervals[0][1]]
            heapq.heapify(end_times)
            room=1
            for i in range(1, len(intervals)):

                start_time= intervals[i][0]
                if start_time  < end_times[0]:
                    heapq.heappush(end_times, intervals[i][1])
                    room= room +1
                else:
                    heapq.heappop(end_times)
                    heapq.heappush(end_times, intervals[i][1])

            return room


obj=Solution()
print(obj.minMeetingRooms(intervals))


