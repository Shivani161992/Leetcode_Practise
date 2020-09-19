from typing import List

nums = [-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            current_element= nums[i]
            current_max = max(current_element , current_element + current_max)
            if current_max > global_max:
                global_max = current_max

        return global_max
        
        
obj = Solution()
print(obj.maxProduct(nums))