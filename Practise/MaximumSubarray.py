from typing import List
nums = [-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        gmax=nums[0]
        lmax=nums[0]
        for i in range(0, len(nums)):
            current=nums[i]
            lmax=max(lmax+current, current)
            if lmax > gmax:
                gmax=lmax
        return gmax


obj=Solution()
print(obj.maxSubArray(nums))
