from typing import List
nums=[1,2,3,4]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        main=[[]]
        for i in range(0, len(nums)):
            hold=[]
            for j in range(i, len(nums)):
                #hold = hold + str(nums[j])
                hold.append(nums[j])
                main.append(hold.copy())



        return main

o=Solution()
y=o.subsets(nums)
print(y)