from typing import List
s = 7
nums = [2,3,1,2,4,3]
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        min_sub=len(nums)
        subarray=[]
        idx= 0
        while idx != len(nums)+1:
            if sum(subarray) < s:
                subarray.append(nums[idx])
                idx= idx + 1
            elif sum(subarray) >= s:
                min_sub= min(min_sub, len(subarray))
                subarray.pop(0)
        return min_sub




obj=Solution()
print(obj.minSubArrayLen(s, nums))
