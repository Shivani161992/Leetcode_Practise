from typing import List
nums = [-1,-1,-1,0,1,1]
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            x= sum(nums[:i])
            y= sum(nums[i+1:])
            if x==y:
                return i
        return -1
    "hello siddharth singh"

o=Solution()
y=o.pivotIndex(nums)
print(y)