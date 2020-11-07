from typing import List
n=5
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return []
        elif rowIndex == 1:
            return [[1]]
        elif rowIndex == 2:
            return [[1], [1,1]]
        elif rowIndex > 2:
            tri=[[1], [1,1]]

obj=Solution()
print(obj.getRow(n))
