from typing import List
grid=[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=0
        row=len(grid)
        col=len(grid[0])
        for r in range(0, row):
            for c in range(0, col):
                ptotal=4
                up = 0
                bottom = 0
                left = 0
                right = 0
                if grid[r][c]==1:
                    # check top element
                    if r-1 >= 0 and grid[r-1][c]==1 :
                        up = 1
                    #check bottom element
                    if r+1 <= row-1 and grid[r+1][c]==1:
                        bottom = 1
                     #check left element
                    if c-1 >=0 and grid[r][c-1]==1:
                        left =1
                    # check right element
                    if c + 1 <= col-1 and grid[r][c+1] == 1:
                        right =1

                    perimeter= perimeter + (ptotal - (up+bottom+left+right))
        return perimeter
obj=Solution()
print(obj.islandPerimeter(grid))