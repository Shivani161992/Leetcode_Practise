from typing import List

maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [3, 2]


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = ""
        r = start[0] + 1
        c = start[1] + 1
        destination[0]= destination[0]+1
        destination[1] = destination[1] + 1
        maze.append([1] * len(maze[0]))
        maze.insert(0, ([1] * len(maze[0])))
        for i in range(len(maze)):
            maze[i].append(1)
            maze[i].insert(0, 1)
        haspaths = self.stop(maze, r, c, destination, directions)
        return haspaths

    def stop(self, maze, r, c, destination, directions):
        if (r >= 0 and r < len(maze) and c >= 0 and c < len(maze)):
            if directions == "":
                right = self.stop(maze, r, c + 1, destination, "right")
                down = self.stop(maze, r + 1, c, destination, "down")
                left = self.stop(maze, r, c - 1, destination, "left")
                up = self.stop(maze, r - 1, c, destination, "up")
                if right == True or down == True or left == True or up == True:
                    return True
                else:
                    return False
            elif directions != "":
                if maze[r][c] == 1:
                    return False
                elif maze[r][c] == 0:
                    if (r == (destination[0])) and (c == (destination[1] )):
                        dir = {"up": [1, 0], "right": [0, 1], "down": [-1, 0], "left": [0, -1]}
                        x= maze[r + dir[directions][0]][c + dir[directions][1]]
                        if (maze[r + dir[directions][0]][c + dir[directions][1]] == 1):
                            return True
                        elif (maze[r + dir[directions][0]][c + dir[directions][1]] == 0):
                            return False
                    else:
                        maze[r][c] = 2
                        right = self.stop(maze, r, c + 1, destination, "right")
                        down = self.stop(maze, r + 1, c, destination, "down")
                        left = self.stop(maze, r, c - 1, destination, "left")
                        up = self.stop(maze, r - 1, c, destination, "up")
                        if right == True or down == True or left == True or up == True:
                            return True
                        else:
                            return False
        else:
            return False


obj = Solution()
print(obj.hasPath(maze, start, destination))
