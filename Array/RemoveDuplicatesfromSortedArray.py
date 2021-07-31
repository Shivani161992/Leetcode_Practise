nums = [1,1,2]
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return nums
        else:
            i=0
            for k in range(0, len(nums)):
                if k !=i:
                    if nums[i]!=nums[k]:
                        nums[i+1]=nums[k]
                        i= i+1
            return i+1



obj=Solution()
print(obj.removeDuplicates(nums))


