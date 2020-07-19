from typing import List
nums = [1,1,1,2,2,3]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=0
        prev = None
        len_nums =len(nums)
        count = 0
        for i in range(0, len_nums):
            if prev != nums[index]:
                prev = nums[index]
                count=1
                index += 1

            else:
                if count < 2:
                    prev = nums[index]
                    index = index + 1
                    count = count  + 1
                else:
                    nums.pop(index)
                    len_nums= len(nums)

        return len(nums)




o=Solution()
y=o.removeDuplicates(nums)
print(y)