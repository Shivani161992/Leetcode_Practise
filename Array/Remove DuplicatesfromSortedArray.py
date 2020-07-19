from typing import List

nums = [1, 1, 2]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_length=len(nums)
        index= 0
        prev = -100
        for i in range (0, nums_length):
            if prev != nums[index]:
                prev = nums[index]
                index += 1
            elif prev == nums[index]:
                nums.pop(index)
                nums_length=len(nums)

        return len(nums)

o=Solution()
y=o.removeDuplicates(nums)
print(y)