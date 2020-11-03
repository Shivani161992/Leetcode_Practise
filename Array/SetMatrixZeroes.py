from typing import List
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])

        for r in range(row):
            for c in range(col):




obj=Solution()
print(obj.setZeroes(matrix))
