from typing import List

grid = [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortestPath = 0
        if len(grid) == 0:
            return shortestPath
        else:
            row = len(grid)
            col = len(grid[0])
            r = 0
            c = 0
            if grid[r][c] == 0 and grid[row - 1][col - 1] == 0:
                shortestPath = self.path(grid, r, c, shortestPath)
                return shortestPath
            else:
                return 0

    def path(self, grid, r, c, shortestPath):
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
            if grid[r][c] == 0:
                grid[r][c]=-1
                shortestPath = shortestPath + 1
                if (r == len(grid) - 1) and (c == len(grid[0]) - 1):
                    return shortestPath
                dia1 = self.path(grid, r + 1, c + 1, shortestPath)
                if dia1 !=0:
                    return dia1
                bottom = self.path(grid, r + 1, c, shortestPath)
                if bottom !=0:
                    return bottom
                right = self.path(grid, r, c + 1, shortestPath)
                if right != 0:
                    return right
                dia2 = self.path(grid, r - 1, c + 1, shortestPath)
                if dia2 != 0:
                    return dia2
                up = self.path(grid, r - 1, c, shortestPath)
                if up != 0:
                    return up
            else:
                return 0
        else:
            return 0


obj = Solution()
print(obj.shortestPathBinaryMatrix(grid))
