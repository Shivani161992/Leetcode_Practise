from typing import List
nums = [-2,3,-4]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_product = nums[0]
        global_product = nums[0]
        for i in range(1, len(nums)):
            a= nums[i] * current_product
            b= nums[i]
            current_product = max(nums[i], nums[i] * current_product)
            if current_product > global_product:
                global_product = current_product

        return global_product




obj= Solution()
print(obj.maxProduct(nums))
