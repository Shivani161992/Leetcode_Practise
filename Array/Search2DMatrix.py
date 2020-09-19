from typing import List
matrix = []
target = 0
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        else:
            col= len(matrix[0])
            left= 0
            right = (len(matrix) * len(matrix[0])) - 1
            while left <= right:
                mid = left + (right - left ) //2
                mid_row = mid // col
                mid_col = mid % col
                if matrix[mid_row][mid_col] == target:
                    return True
                elif target < matrix[mid_row][mid_col]:
                    right = mid - 1
                elif target > matrix[mid_row][mid_col]:
                    left = mid + 1
            return False


obj= Solution()
print(obj.searchMatrix(matrix, target))

