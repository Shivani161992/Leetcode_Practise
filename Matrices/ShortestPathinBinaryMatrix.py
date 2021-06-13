from typing import List
from collections import deque

grid = [[0,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,1,0,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,0,1,0],[0,0,0,0,0,1,1,0],[1,1,1,1,1,1,1,0]]
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        clearPath = 0
        if len(grid) == 0:
            return clearPath
        elif grid[0][0] != 0:
            return -1
        else:
            dir = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
            bfs = deque()
            bfs.append([0, 0])
            grid[0][0]=1
            while bfs:
                bfslen = len(bfs)
                clearPath = clearPath + 1
                for p in range(0, bfslen):
                    point = bfs.popleft()
                    for d in dir:
                        pr = point[0] + d[0]
                        pc = point[1] + d[1]
                        if pr >=0 and pr < len(grid) and pc >=0 and pc < len(grid[0]) and grid[pr][pc]==0:
                            if pr== len(grid)-1 and pc== len(grid[0])-1:
                                return clearPath + 1
                            else:
                                grid[pr][pc] = 1
                                bfs.append([pr, pc])
            return -1

obj = Solution()
print(obj.shortestPathBinaryMatrix(grid))
