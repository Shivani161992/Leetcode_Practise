from typing import List
nums= [1,1,0,1,1,1]
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)
        con_max = 0
        while len(nums) != 0:
            if (0 in nums):
                pos=nums.index(0)
                con_max = max(con_max, len(nums[:pos]))
            elif 0 not in nums:
                con_max = max(con_max, len(nums))
            nums = nums[pos+1:]

        return con_max




o=Solution()
y=o.findMaxConsecutiveOnes(nums)
print(y)
