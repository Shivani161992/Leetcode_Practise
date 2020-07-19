from typing import List
nums  = [1]
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if (len(nums)==0):
            return 1
        else:
            nums.sort()
            index = 1
            for i in range(0, len(nums)):
                if index ==  nums[i]:
                    index = index +1
                elif index !=  nums[i]:
                    if nums[i] > index:
                        return index


            return index


o=Solution()
y=o.firstMissingPositive(nums)
print(y)
