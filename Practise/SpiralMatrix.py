from typing import List
matrix=  [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top=0
        bottom=len(matrix)
        left=0
        right=len(matrix[0])
        elements=len(matrix)*len(matrix[0])
        spiral=[]
        while len(spiral) < elements:
            if len(spiral) < elements:
                #top row
                for i in range(left, right):
                    spiral.append(matrix[top][i])
                top = top +1

            if len(spiral) < elements:
                #for right
                for j in range(top, bottom):
                    spiral.append(matrix[j][right-1])
                right= right -1

            if len(spiral) < elements:
                #for bottom
                for k in range(right-1, left-1, -1):
                    spiral.append(matrix[bottom-1][k])
                bottom=bottom-1
            if len(spiral) < elements:
                #for left
                for l in range(bottom-1, top-1, -1):
                    spiral.append(matrix[l][left])
                left= left + 1

        return spiral




o=Solution()
y=o.spiralOrder(matrix)
print(y)


