nums = [1, -1, 0]
k = 0
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) >0:
            totabSubarray=0
            for i in range(0, len(nums)):
                subArr= 0
                for j in range(i, len(nums)):
                    subArr= subArr + nums[j]
                    if subArr == k:
                        totabSubarray= totabSubarray + 1
            return totabSubarray

        #hashMap solution
        count = 0
        sumarr = 0
        dic = {0: 1}
        for n in nums:
            sumarr = sumarr + n
            if sumarr - k in dic:
                count = count + dic[sumarr - k]
            if sumarr in dic:
                dic[sumarr] = dic[sumarr] + 1
            else:
                dic[sumarr] = +1
        return count


obj=Solution()
print(obj.subarraySum(nums, k))
