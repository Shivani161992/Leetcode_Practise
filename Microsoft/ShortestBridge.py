from typing import List

grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        cord = []
        shortestpath = 0
        foundIsland = False
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    foundIsland = True
                    self.getIsland(r, c, grid, cord)
                    break
            if foundIsland == True:
                break

        while cord:
            getCordSize = len(cord)
            for i in range(getCordSize):
                getCord = cord.pop(0)
                cordR = getCord[0]
                cordC = getCord[1]
                if self.valid(cordR + 1, cordC, grid) == True:
                    if grid[cordR + 1][cordC] == 0:
                        grid[cordR + 1][cordC] = grid[cordR][cordC] + 1
                        cord.append([cordR + 1, cordC])
                    elif grid[cordR + 1][cordC] == 1:
                        return shortestpath
                if self.valid(cordR - 1, cordC, grid) == True:
                    if grid[cordR - 1][cordC] == 0:
                        grid[cordR - 1][cordC] = grid[cordR][cordC] + 1
                        cord.append([cordR - 1, cordC])
                    elif grid[cordR - 1][cordC] == 1:
                        return shortestpath
                if self.valid(cordR, cordC + 1, grid) == True:
                    if grid[cordR][cordC + 1] == 0:
                        grid[cordR][cordC + 1] = grid[cordR][cordC] + 1
                        cord.append([cordR, cordC + 1])
                    elif grid[cordR][cordC + 1] == 1:
                        return shortestpath
                if self.valid(cordR, cordC - 1, grid) == True:
                    if grid[cordR][cordC - 1] == 0:
                        grid[cordR][cordC - 1] = grid[cordR][cordC] + 1
                        cord.append([cordR, cordC - 1])
                    elif grid[cordR][cordC - 1] == 1:
                        return shortestpath
            shortestpath = shortestpath + 1
        return shortestpath

    def getIsland(self, r, c, grid, cord):
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
            if grid[r][c] == 1:
                if self.isvalid(r + 1, c, grid) == True or \
                        self.isvalid(r - 1, c, grid) == True or \
                        self.isvalid(r, c + 1, grid) == True or \
                        self.isvalid(r, c - 1, grid) == True:
                    grid[r][c] = grid[r][c] + 1
                    cord.append([r, c])
                else:
                    grid[r][c] = "#"
                self.getIsland(r + 1, c, grid, cord)
                self.getIsland(r - 1, c, grid, cord)
                self.getIsland(r, c + 1, grid, cord)
                self.getIsland(r, c - 1, grid, cord)
                return
            else:
                return
        else:
            return

    def isvalid(self, r, c, grid):
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
            if grid[r][c] == 0:
                return True
            else:
                return False
        else:
            return False

    def valid(self, r, c, grid):
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
            return True
        else:
            return False


obj = Solution()
print(obj.shortestBridge(grid))
