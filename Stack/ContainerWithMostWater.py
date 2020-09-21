from typing import List
height= [1,8,6,2,5,4,8,3,7]
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        low=0
        high=len(height) -1
        while low != high:
            length= height[low] if height[low] <= height[high] else height[high]
            breadth= high - low
            area= length * breadth
            max_area= max(max_area, area)
            if height[low] < height[high]:
                low = low + 1
            elif height[low] >= height[high]:
                high = high - 1

        return max_area


obj= Solution()
print(obj.maxArea(height))