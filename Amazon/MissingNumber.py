from typing import List

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            totalSum = 0
            givenSum = 0
            count = 0
            for n in nums:
                count = count + 1
                totalSum = totalSum + count
                givenSum = givenSum + n
            #formula based answer
            f= len(nums)
            stotal= (f*(f +1))//2
            sum_local= sum(nums)
            return stotal - sum_local


obj = Solution()
print(obj.missingNumber(nums))
