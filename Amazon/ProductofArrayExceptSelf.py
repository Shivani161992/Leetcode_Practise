from typing import List
nums= [1,2,3,4]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hold_left=[]
        hold_right=[]

        #here the concept is to find the product of all the elements of left side of the index
        #and the product of all the elements of right side and then multiple them

        #for all the left side element
        for i in range(0, len(nums)):
            if i == 0:
                hold_left.append(1)
            else:
                get_ele=hold_left[-1]
                hold_left.append(get_ele * nums[i-1])

        # for all the right side elements
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                hold_right.append(1)
            else:
                get_ele=hold_right[0]
                #insert in the begning because we are starting from the last element
                hold_right.insert(0, get_ele * nums[i+1])

        #multiplication of all the left elements and all the right elements
        for i in range(0, len(nums)):
            hold_right[i]= hold_right[i] * hold_left[i]

        return hold_right





obj=Solution()
print(obj.productExceptSelf(nums))