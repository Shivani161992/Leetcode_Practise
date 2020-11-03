from typing import List
height = [1,2,1]
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water=0
        if len(height) == 0:
            return max_water
        low=0
        high=len(height)-1
        while low <= high:
            length=min(height[low], height[high])
            breadth= high-low
            area= length * breadth
            max_water= max(area, max_water)
            if height[low] <= height[high]:
                low= low + 1
            elif height[low] > height[high]:
                high= high - 1
        return max_water



obj=Solution()
print(obj.maxArea(height))
