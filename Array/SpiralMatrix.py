from typing import List
matrix=  [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        hold = []
        if len(matrix) == 0:
            return hold
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        elements = (right + 1) * (bottom + 1)
        while len(hold) < elements:
            if len(hold) < elements:
                for i in range(left, (right + 1)):
                    hold.append(matrix[top][i])
                top = top + 1

            if len(hold) < elements:
                for j in range(top, (bottom + 1)):
                    hold.append(matrix[j][right])
                right = right - 1

            if len(hold) < elements:
                for k in range(right, left - 1, -1):
                    hold.append(matrix[bottom][k])
                bottom = bottom - 1
            if len(hold) < elements:
                for l in range(bottom, top - 1, -1):
                    hold.append(matrix[l][left])
                left = left + 1
        return hold

o=Solution()
y=o.spiralOrder(matrix)
print(y)
