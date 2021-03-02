from typing import List

matrix = [["0","0","0","1","0","1","1","1"],["0","1","1","0","0","1","0","1"],["1","0","1","1","1","1","0","1"],["0","0","0","1","0","0","0","0"],["0","0","1","0","0","0","1","0"],["1","1","1","0","0","1","1","1"],["1","0","0","1","1","0","0","1"],["0","1","0","0","1","1","0","0"],["1","0","0","1","0","0","0","0"]]


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if (len(matrix) == 0):
            return 0
        else:
            garea = 0
            row = len(matrix)
            col = len(matrix[0])
            for r in range(row):
                for c in range(col):
                    if int(matrix[r][c]) == 1:
                        area = self.get_area(matrix, r, c)
                        garea = max(garea, area)
            return garea

    def get_area(self, matrix, r, c):
        larea = 1
        if (c + 1 < len(matrix[0])) and (r + 1 < len(matrix)):
            top_r = r
            top_c = c + 1
            bottom_r = r + 1
            bottom_c = c
            breadth = 1
            while int(matrix[top_r][top_c]) == 1 and int(matrix[bottom_r][bottom_c]) == 1:
                tr = top_r
                tc = top_c
                br = bottom_r
                bc = bottom_c
                complete = False

                while tr != br or tc != bc:
                    if int(matrix[tr][tc]) == 1 and int(matrix[br][bc]) == 1:
                        tr = tr + 1
                        bc = bc + 1
                    elif int(matrix[tr][tc]) == 0 or int(matrix[br][bc]) == 0:
                        break
                    if (tr == br and tc == bc) and  (int(matrix[tr][tc]) == 1 and int(matrix[br][bc]) == 1):
                        complete = True
                if complete == True:
                    breadth = breadth + 1
                    larea = breadth * breadth
                elif complete == False:
                    break
                if (top_c + 1 < len(matrix[0])) and (bottom_r+1 < len(matrix)):
                    top_c = top_c + 1
                    bottom_r = bottom_r + 1
                else:
                    break

        return larea

    def maximalSquareDP(self, matrix: List[List[str]]) -> int:
        print()


obj = Solution()
print(obj.maximalSquare(matrix))
