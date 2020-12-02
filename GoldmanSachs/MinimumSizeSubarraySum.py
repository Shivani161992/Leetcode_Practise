from typing import List
s = 7
nums = [2,3,1,2,4,3]
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s or s ==0:
            return 0
        else:
            sidx= 0
            msubarray= len(nums) + 1
            for eidx in range(len(nums)):
                subarray= nums[sidx:eidx+1]
                while sum(nums[sidx:eidx+1]) >=s:
                    msubarray= min(msubarray, len(nums[sidx:eidx+1]))
                    sidx= sidx + 1
            return msubarray






obj=Solution()
print(obj.minSubArrayLen(s, nums))
