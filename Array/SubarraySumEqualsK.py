from typing import List
nums = [-1, -1, 1]
k = 0
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        startidx = 0
        count = 0
        if len(nums)==0:
            return count
        for i in range(0, len(nums)):
            subarr= nums[startidx : i+1]
            while sum(subarr) >=k:
                if sum(subarr) ==k:
                    count = count + 1
                startidx= startidx + 1
                subarr = nums[startidx: i + 1]

        return count

obj=Solution()
print(obj.subarraySum(nums, k))