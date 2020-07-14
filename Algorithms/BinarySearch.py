from typing import List
num=[1]
target = 2
class Solution:
    def binarysearch(self, num: List[int], target) -> int:
        low=0
        high = len(num) -1
        while low <= high:
            mid = low + (high - low) //2
            if num[mid] == target:
                return mid
            elif target < num[mid]:
                high = mid - 1
            elif target > num [mid]:
                low = mid + 1

        return -1

o=Solution()
y=o.binarysearch(num, target)
print(y)