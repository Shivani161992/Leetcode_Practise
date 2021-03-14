from typing import List

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

class Solution:
    def rotate(self, matrix: List[List[int]]):
        if len(matrix) == 0:
            return matrix
        else:
            top = 0
            bottom = len(matrix) - 1
            constant= len(matrix) - 1
            while top < bottom:
                i = top
                j = bottom
                for c in range(0, constant):
                    temp1 = matrix[i][i + c]
                    temp2 = matrix[i + c][j]
                    matrix[i][i + c] = matrix[j - c][i]
                    matrix[i + c][j] = temp1
                    temp1 = matrix[j][j - c]
                    matrix[j][j - c] = temp2
                    matrix[j - c][i] = temp1

                top = top + 1
                bottom = bottom - 1
                constant= constant -2



obj = Solution()
print(obj.rotate(matrix))
