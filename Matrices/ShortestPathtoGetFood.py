from typing import List
from collections import deque

grid = [["X","*"],["#","X"]]

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        steps = 0
        row = len(grid)
        col = len(grid[0])
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c] == '*':
                    bfs = deque()
                    bfs.append([r,c])
                    while bfs:
                        level = len(bfs)
                        steps = steps + 1
                        for l in range(0, level):
                            point = bfs.popleft()
                            for d in dir:
                                pr = point[0] + d[0]
                                pc = point[1] + d[1]
                                if pr >= 0 and pr < len(grid) and pc >= 0 and pc < len(grid[0]) and grid[pr][pc] == 'O' :
                                    grid[pr][pc] ='X'
                                    bfs.append([pr, pc])
                                elif pr >= 0 and pr < len(grid) and pc >= 0 and pc < len(grid[0]) and grid[pr][pc] == '#':
                                    return steps
        return -1


obj = Solution()
print(obj.getFood(grid))
