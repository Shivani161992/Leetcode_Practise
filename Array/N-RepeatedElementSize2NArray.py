from typing import List

A=[5,1,5,2,5,3,5,4]
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        seen=set()
        for i in A:
            if i in seen:
                return i
            else:
                seen.add(i)



o=Solution()
y=o.repeatedNTimes(A)
print(y)