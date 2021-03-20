from typing import List
nums = [0,1,2,2,3,0,4,2]
val = 2
class Solution:
    def removeElement(self, nums: List[int], val: int):
        if len(nums) == 0 and len(nums):
            return 0
        else:
            i = 0
            j = len(nums)
            while i < j:
                if nums[i] == val:
                    nums[i] = nums[j - 1]
                    j = j - 1
                else:
                    i = i + 1

            return j
obj = Solution()
print(obj.removeElement(nums, val))
