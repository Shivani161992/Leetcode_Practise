from typing import List
nums = [1,7,3,6,5,6]
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        globalSum= sum(nums)
        localSum=0
        for idx, n in enumerate(nums):
            if localSum == globalSum- (localSum + n):
                return idx
            else:
                localSum= localSum + n

        return -1

o=Solution()
print(o.pivotIndex(nums))
