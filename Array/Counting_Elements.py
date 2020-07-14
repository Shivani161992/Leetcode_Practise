from typing import List
arr = [1,1,3,3,5,5,7,7]
class Solution:
    def countElements(self, arr: List[int]) -> int:
        element=0
        for i in arr:
            if i+1 in arr:
                element= element+1;

        return element


o=Solution()
y=o.countElements(arr)
print(y)