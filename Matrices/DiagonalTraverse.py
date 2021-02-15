from typing import List

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        diagonalTraversal = []
        if len(matrix) == 0:
            return diagonalTraversal
        else:
            direc = 'left'
            r = 0
            c = 0
            row = len(matrix)
            col = len(matrix[0])
            elements = row * col
            diagonalTraversal.append(matrix[r][c])
            while len(diagonalTraversal) != elements:
                if direc == 'left':
                    direc = 'right'
                    if (c + 1 < col):
                        c = c + 1
                        diagonalTraversal.append(matrix[r][c])
                    elif (c == col-1) and (r < row):
                        r = r + 1
                        diagonalTraversal.append(matrix[r][c])
                    while (r + 1 < row) and (c - 1 >= 0):
                        r = r + 1
                        c = c - 1
                        diagonalTraversal.append(matrix[r][c])
                elif direc == 'right':
                    direc = 'left'
                    if (r + 1 < row):
                        r = r + 1
                        diagonalTraversal.append(matrix[r][c])
                    elif (r  == row-1) and (c < col) :
                        c = c + 1
                        diagonalTraversal.append(matrix[r][c])
                    while (r - 1 >= 0) and (c + 1 < col):
                        r = r - 1
                        c = c + 1
                        diagonalTraversal.append(matrix[r][c])
            return diagonalTraversal



obj = Solution()
print(obj.findDiagonalOrder(matrix))
