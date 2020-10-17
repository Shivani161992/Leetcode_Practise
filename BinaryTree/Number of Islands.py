from typing import List
grid =[["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands =0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] =='1':
                    x = self.island_dfs(grid, i, j)
                    if x > 0:
                        islands = islands + 1
        return islands

    def island_dfs(self, grid, i, j):
        count=0
        if (i >=0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j]=='1'):
            grid[i][j] = '0'
            count=1
            count = count + self.island_dfs(grid, i-1, j)
            count = count + self.island_dfs(grid, i+1, j)
            count = count + self.island_dfs(grid, i, j-1)
            count = count + self.island_dfs(grid, i, j+1)

        return count

o=Solution()
y=o.numIslands(grid)
print(y)