from typing import List
nums = [-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        gmax=nums[0]
        lmax=nums[0]
        for i in range(1, len(nums)):
            lmax = max(nums[i], lmax + nums[i])
            gmax = gmax if gmax >= lmax else lmax
        return gmax




obj = Solution()
print(obj.maxSubArray(nums))




