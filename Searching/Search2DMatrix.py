from typing import List
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print()

o=Solution()
y=o.searchMatrix(matrix, target)
print(y)