from typing import List
import heapq as h

sticks = [5]
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minCost = 0
        if len(sticks) == 1:
            return minCost
        else:
            h.heapify(sticks)
            while len(sticks) != 1:
                min1 = h.heappop(sticks)
                min2 = h.heappop(sticks)
                combineCost = min1 + min2
                minCost = minCost + combineCost
                h.heappush(sticks, combineCost)

            return minCost


obj = Solution()
print(obj.connectSticks(sticks))
