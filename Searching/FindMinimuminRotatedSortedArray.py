nums=[4,5,6,7,0,1,2]
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while nums[low] > nums[high]:
            mid = low + (high-low) //2
            if nums[mid] < nums[high]:
                high=mid
            else:
                low=mid+1
        return nums[low]


obj=Solution()
print(obj.findMin(nums))
