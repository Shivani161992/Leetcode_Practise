from typing import List
grid=[[0]]
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        two=0
        lqueue = []
        row = len(grid)
        col = len(grid[0])
        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c]==2:
                    lqueue.append([r,c])

        while len(lqueue)!=0:
            two=1
            len_queue = len(lqueue)
            for q in range(0, len_queue):
                get= lqueue.pop(0)
                #for upper element
                if get[0]-1 >= 0 and grid[get[0]-1][get[1]]==1 :
                    grid[get[0] - 1][get[1]]=2
                    lqueue.append([get[0] - 1, get[1]])
                #for lower element
                if get[0]+1 < row and grid[get[0]+1][get[1]]==1 :
                    grid[get[0] + 1][get[1]]=2
                    lqueue.append([get[0] + 1, get[1]])
                #for left element
                if get[1]-1 >= 0 and grid[get[0]][get[1]-1]==1 :
                    grid[get[0]][get[1] -1]=2
                    lqueue.append([get[0], get[1] -1])

                # for right element
                if get[1] + 1 < col and grid[get[0]][get[1] + 1] == 1 :
                    grid[get[0]][get[1] + 1] = 2
                    lqueue.append([get[0], get[1] + 1])
            minute = minute + 1
        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c]==1:
                    return -1

        if two==1:
            return minute-1
        else:
            return minute






obj=Solution()
print(obj.orangesRotting(grid))