nums = [-2,1,-3,4,-1,2,1,-5,4]
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        gmax=nums[0]
        lmax=nums[0]
        for n in range(1, len(nums)):
            lmax=max(nums[n], lmax+nums[n])
            if lmax > gmax:
                gmax= lmax
        return gmax

obj=Solution()
print(obj.maxSubArray(nums))
