from typing import List

nums = [[1,2,3],[4,5,6],[7,8,9]]

from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diatra = []
        if len(nums) == 0:
            return diatra
        elif len(nums) == 1:
            return nums[0]
        else:
            default = defaultdict(list)
            for r in range(0, len(nums)):
                for c in range(0, len(nums[r])):
                    default[r + c].append(nums[r][c])
            diatra = [default[d][::-1] for d in default]
            diatra = [y for x in diatra for y in x]
            return diatra


obj = Solution()
print(obj.findDiagonalOrder(nums))
