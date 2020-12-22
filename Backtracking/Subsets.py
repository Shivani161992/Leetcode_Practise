from typing import List
nums=[1,2,3]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets=[[]]
        for n in nums:
            for i in range(0, len(sets)):
                get_set = sets[i].copy()
                get_set.append(n)
                sets.append(get_set)

        return sets

obj=Solution()
obj.subsets(nums)