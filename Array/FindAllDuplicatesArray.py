from typing import List
nums = [1,1]
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hold = []
        if len(nums)== 0 or len(nums)==1:
            return hold

        nums.sort()
        prev=nums[0]
        nums_len = len(nums)
        for i in range(1, nums_len):
            value= nums[i]
            if value==prev:
                hold.append(value)
            else:
                prev=value

        return hold

o=Solution()
y=o.findDuplicates(nums)
print(y)
