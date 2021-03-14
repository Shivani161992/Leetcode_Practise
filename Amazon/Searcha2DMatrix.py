from typing import List

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 15


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        else:
            low = 0
            high = (len(matrix) * len(matrix[0])) - 1
            col = len(matrix[0])
            while low <= high:
                mid= (high+low) //2
                r= mid//col
                c= mid%col
                if matrix[r][c] == target:
                    return True
                elif target < matrix[r][c]:
                    high= mid -1
                elif target > matrix[r][c]:
                    low = mid +1
            return False



obj = Solution()
print(obj.searchMatrix(matrix, target))
