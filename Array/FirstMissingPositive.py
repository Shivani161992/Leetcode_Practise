from typing import List
nums  = [-1, -3]
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if (len(nums)==0):
            return 1
        else:
            x=[i for i in set(nums) if i >=0]
            if (len(x)==0):
                return 1
            else:
                maximum = max(set(x))
                y = [i for i in range(1, maximum+1)]
                z=set(y) - set(x)
                if len(z)==0:
                    return maximum+1
                else:
                    return z.pop()
o=Solution()
y=o.firstMissingPositive(nums)
print(y)
