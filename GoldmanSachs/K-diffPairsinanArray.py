from typing import List
nums = [-1,-2,-3]
k = 1
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs=0
        if len(nums) > 1:
            key_val=dict(Counter(nums).most_common())
            for i in key_val.keys():
                a=(i + k)
                b=key_val.keys()
                if k > 0 and (i+ k) in key_val.keys():
                    pairs = pairs + 1
                elif k ==0 and len(i[0]) > 1:
                    pairs= pairs + 1
        return pairs

obj=Solution()
print(obj.findPairs(nums, k))