from typing import List
nums = [1,3]
target = 3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low <= high:
            mid_ele= low + (high -low) //2
            if nums[mid_ele] == target:
                return mid_ele
            elif nums[low] <= nums[mid_ele]:
                if target >= nums[low] and target < nums[mid_ele]:
                    high= mid_ele - 1
                else:
                    low= mid_ele + 1
            else:
                if nums[mid_ele] < target and target <= nums[high]:
                    low = mid_ele + 1
                else:
                    high = mid_ele - 1

        return -1




obj=Solution()
print(obj.search(nums, target))
