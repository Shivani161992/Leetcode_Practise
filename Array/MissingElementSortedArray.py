from typing import List
nums = [1,2,4]
k = 3
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        idx=0
        count=0
        start= nums[0]
        end = len(nums)-1
        while idx != end:
            start = start + 1
            if idx >= len(nums)-1:
                count = count + 1
                if count == k:
                    return start
            elif idx < len(nums)-1:
                if start != nums[idx + 1]:
                    count= count + 1
                    if count == k:
                        return start
                elif start == nums[idx +1]:
                    idx= idx + 1
                    if idx == end:
                        end = end + 1



obj= Solution()
print(obj.missingElement(nums, k))
