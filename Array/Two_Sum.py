nums = [2, 7, 11, 15]
target = 9
class Solution(object):
    def twoSum(self, nums, target):
        for k, v in enumerate(nums):
            diff=target-v
            if diff in nums:
                sec_ind=nums.index(diff)
                if (k!=sec_ind):
                    return [k, sec_ind]




o=Solution()
y=o.twoSum(nums, target)
print(y)