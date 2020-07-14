from typing import List
x=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum_area=0
        for i in range (0, len(grid)):
            for j in range (0, len(grid[0])):
                if grid[i][j]==1:
                    maximum_area=max(maximum_area, self.dfs_maximum_area(grid, i , j))

        return maximum_area

    def dfs_maximum_area(self, grid, i , j):
        area=0
        if (i >=0 and i <len(grid) and j >=0 and j <len(grid[0]) and grid[i][j]==1):
            grid[i][j] = 0
            area=1
            area= area + self.dfs_maximum_area(grid, i -1 , j)
            area = area + self.dfs_maximum_area(grid, i +1, j)
            area = area + self.dfs_maximum_area(grid, i, j -1)
            area = area + self.dfs_maximum_area(grid, i, j +1)

        return area




o=Solution()
y=o.maxAreaOfIsland(x)
print(y)