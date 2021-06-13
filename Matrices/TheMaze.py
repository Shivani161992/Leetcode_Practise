from typing import List

maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0, 4]
destination = [1, 2]


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dict = {'u': [-1, 0], 'd': [1, 0], 'r': [0, 1], 'l': [0, -1]}
        sr = start[0]
        sc = start[1]

        stopped = self.dfs(dict, sr, sc, maze, destination, '')
        return stopped

    def dfs(self, dict, sr, sc, maze, destination, dir):
        if sr >= 0 and sr < len(maze) and sc >= 0 and sc < len(maze[0]):
            if maze[sr][sc] == 0:
                if sr == destination[0] and sc == destination[1]:
                    print(sr, sc, dir)
                    rollingR = sr + dict[dir][0]
                    rollingC = sc + dict[dir][1]
                    print(rollingR, rollingC, dir)
                    if rollingR < 0 or rollingR >= len(maze) or rollingC < 0 or rollingC >= len(maze[0]) or maze[rollingR][rollingR]==1:
                        return True
                    else:
                        False
                else:

                    maze[sr][sc] = 1
                    for d in dict:
                        getDir = dict[d]
                        newR = sr + getDir[0]
                        newC = sc + getDir[1]
                        if newR >= 0 and newR < len(maze) and newC >= 0 and newC < len(maze[0]):
                            if maze[newR][newC] == 0:
                                stopped = self.dfs(dict, newR, newC, maze, destination, d)
                                if stopped==True:
                                 return stopped
                    maze[sr][sc] = 0
                    return False
            else:
                return False


obj = Solution()
print(obj.hasPath(maze, start, destination))
