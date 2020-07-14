from collections import Counter
from typing import List
nums= [1, 2, 2, 3, 1]
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq= Counter(nums).most_common()
        degree=freq[0][1]
        min_subarray=len(nums)
        elements=[]
        for i in freq:
            if degree==i[1]:
                elements.append(i[0])
            elif degree!=i[1]:
                break
        for i in range(0, len(elements)):
            first=nums.index(elements[i])
            last=(len(nums)-1) - nums[::-1].index(elements[i])
            min_subarray = min (min_subarray, len(nums[first:last+1]))

        return min_subarray


o=Solution()
y=o.findShortestSubArray(nums)
print(y)