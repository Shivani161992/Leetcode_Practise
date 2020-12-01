nums= [0,1,0,3,12]
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 0 or sum(nums) == 0:
            return nums
        else:
            midx= 0
            idx= 0
            while midx < len(nums):
                if nums[midx] !=0:
                    nums[idx]= nums[midx]
                    idx= idx + 1
                midx= midx + 1

            while idx < len(nums):
                nums[idx]=0
                idx = idx + 1






obj=Solution()
print(obj.moveZeroes(nums))


