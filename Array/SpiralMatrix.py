from typing import List
matrix= [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_traversal=[]
        elements = len(matrix) * len(matrix[0]) # 9
        spiral_elements= len(spiral_traversal)
        top=0
        left=0
        bottom=len(matrix) - 1 # 2
        right=len(matrix[0]) - 1 # 2
        hold2 = len(matrix[0]) - 1
        while spiral_elements < elements:
            #for top
            for i in matrix[top]:
                spiral_traversal.append(i)
            top= top + 1

            #for right


            while top <= bottom:
                spiral_traversal.append(matrix[top][right])
                top=top +1
            right = right - 1

            #for bottom
            for k in matrix[bottom ]:
                spiral_traversal.append(k)
            bottom= bottom - 1

            #for left
            for l in matrix[left]:
                spiral_traversal.append(l)
            left= left + 1


        return spiral_traversal


o=Solution()
y=o.spiralOrder(matrix)
print(y)
