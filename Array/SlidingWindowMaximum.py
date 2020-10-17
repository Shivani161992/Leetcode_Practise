from typing import List
import heapq
nums = [4,-2]
k = 2
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_window = []
        for i in range(0, len(nums)):
            if k + i > len(nums):
                return max_window
            else:
                window = nums[i:k + i]
                heapq.heapify(window)
                heapq._heapify_max(window)
                max_window.append(heapq.heappop(window))
        return max_window

obj=Solution()
print(obj.maxSlidingWindow(nums, k))

