from typing import List
nums=[1,2,3,4]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hold_left=[]
        hold_right=[]

        for i in range(0, len(nums)):
            if i == 0:
                hold_left.append(1)
            elif i != 0:
                get=hold_left[-1]
                hold_left.append(get * nums[i-1])

        for j in range((len(nums)-1), -1, -1):
            if j == len(nums)-1:
                hold_right.append(1)
            elif j != len(nums)-1:
                get = hold_right[0]
                hold_right.insert(0, get*nums[j+1])

        for k in range(0, len(hold_right)):
            hold_right[k]=hold_right[k] * hold_left[k]

        return hold_right

o=Solution()
y=o.productExceptSelf(nums)
print(y)