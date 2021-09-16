from typing import List
nums = [2,3,1,1,4]
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True
        else:
            reachable=0
            for idx, val in enumerate(nums):
                if idx > reachable:
                    return False
                reachable= max(reachable, idx+val)
            return True





obj=Solution()
print(obj.canJump(nums))