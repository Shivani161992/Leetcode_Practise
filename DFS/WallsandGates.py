from typing import List
rooms=[
    [0, 0, float('inf'), float('inf'), 0],
    [-1, float('inf'), 0, 0, 0],
    [float('inf'), 0, -1, 0, float('inf')]
]
# inf empty room
# 0 gate
# -1 wall
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        if len(rooms) == 0:
            return rooms
        row = len(rooms)
        col = len(rooms[0])
        queue=[]
        for r in range(0, row):
            for c in range(0, col):
                if rooms[r][c]==0:
                    queue.append([r,c])
        self.helper(rooms, queue)
        return rooms

    def helper(self, rooms, queue):
        seen=[]
        count = -1
        while len(queue) !=0:
            get_size=len(queue)
            count= count +1
            for ele in range(0, get_size):
                get_ele= queue.pop(0)
                seen.append(get_ele)
                r = get_ele[0]
                c = get_ele[1]
                # set the values now
                rooms[r][c]= min(count, rooms[r][c])
                # up

                if r-1 >= 0 and rooms[r-1][c] != -1 and rooms[r-1][c] != 0:
                    in_seen=[r-1, c]
                    if in_seen not in seen:
                        queue.append([r-1, c])
                #down

                if r+1 <len(rooms) and rooms[r+1][c] != -1 and rooms[r+1][c] != 0 :
                    in_seen = [r + 1, c]
                    if in_seen not in seen:
                        queue.append([r + 1, c])
                #left

                if c-1 >= 0 and rooms[r][c-1] != -1 and rooms[r][c-1] != 0 :
                    in_seen = [r, c - 1]
                    if in_seen not in seen:
                        queue.append([r, c - 1])
                #right

                if c+1 <len(rooms[0]) and rooms[r][c+1] != -1  and rooms[r][c+1] != 0:
                    in_seen = [r, c + 1]
                    if in_seen not in seen:
                        queue.append([r, c + 1])

obj=Solution()
print(obj.wallsAndGates(rooms))