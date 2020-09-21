from typing import List
intervals= [[26,29],[19,26],[19,28],[4,19],[4,25]]
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        h=[intervals[0][1]]
        heapq.heapify(h)
        for i in range(1, len(intervals)):
            pop=h[0]
            start_time= intervals[i][0]
            if start_time >= pop:
                heapq.heappop(h)
                heapq.heappush(h, intervals[i][1])
            elif start_time < pop:
                heapq.heappush(h, intervals[i][1])



        return len(h)

obj=Solution()
print(obj.minMeetingRooms(intervals))
