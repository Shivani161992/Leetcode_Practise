from typing import List
grid=[[0,2]]
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottan=[]
        minute=0
        row=len(grid)
        col=len(grid[0])
        present=0
        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c]==2:
                    rottan.append([r, c])

        while len(rottan) != 0:
            present=1
            cal_min= len(rottan)
            for m in range(0, cal_min):
                get= rottan.pop(0) # get the first element from the queue
                r= get[0]
                c=get[1]

                # check for upper element
                if r-1 >=0 and grid[r-1][c] ==1:
                    grid[r - 1][c]=2
                    rottan.append([r-1, c])
                # for lower element
                if r+1 <row and grid[r+1][c] ==1:
                    grid[r + 1][c]=2
                    rottan.append([r+1, c])
                #for left element
                if c-1 >=0 and grid[r][c-1] ==1:
                    grid[r][c-1]=2
                    rottan.append([r, c-1])
                #for right element
                if c+1<col and grid[r][c+1] ==1:
                    grid[r][c+1]=2
                    rottan.append([r, c+1])

            minute= minute + 1

        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c]==1:
                    return -1

        return minute-1 if present==1 else minute









obj=Solution()
print(obj.orangesRotting(grid))