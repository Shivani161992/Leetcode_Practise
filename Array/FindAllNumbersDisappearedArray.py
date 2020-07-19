from typing import  List
nums = [4,3,2,7,8,2,3,1]
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hold=[]
        set_index=0
        removed_duplicates_sorted=list(set(nums))
        for i in range (1, len(nums)+1):
            if set_index < len(removed_duplicates_sorted):
                if i == removed_duplicates_sorted[set_index]:
                    set_index = set_index +1
                else:
                    hold.append(i)
            else:
                hold.append(i)

        return hold





o=Solution()
y=o.findDisappearedNumbers(nums)
print(y)