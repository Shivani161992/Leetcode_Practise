from typing import List
A=[[1,2,3],[4,5,6],[7,8,9]]
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return zip(*A)

o=Solution()
y=o.transpose(A)
print(y)