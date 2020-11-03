from typing import List
matrix = [[1,1,1],[1,0,1],[1,1,1]]
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[r][c] = '$'

                    for down in range(r+1, row):
                        if matrix[down][c] != 0:
                            matrix[down][c] = '$'
                    for up in range(r-1, -1, -1):
                        if matrix[up][c] != 0:
                            matrix[up][c] = '$'
                    for right in range(c+1, col):
                        if matrix[r][right] != 0:
                            matrix[r][right] = '$'
                    for left in range(c-1, -1, -1):
                        if matrix[r][left] != 0:
                            matrix[r][left] = '$'
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '$':
                    matrix[r][c] = 0







obj=Solution()
print(obj.setZeroes(matrix))
