from typing import List
from collections import OrderedDict

from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food = deque(food)
        self.headR = 0
        self.headC = 0
        self.snake = deque([0,0])
        self.snakeLen = 1
        self.score = 0
        self.width = width
        self.height = height


    def move(self, direction: str) -> int:

        # down, right, left, up
        direc = {'D': [1, 0], 'R': [0, 1], 'U': [-1, 0], 'L': [0, -1]}
        # get move direction
        getDir = direc[direction]
        # increase the coordinates
        self.headR = self.headR + getDir[0]
        self.headC = self.headC + getDir[1]
        # is game over
        if self.headR >= 0 and self.headR < self.height and self.headC >= 0 and self.headC < self.width:
            if len(self.food) >0:
                getFood = self.food[0]
                if self.headR == getFood[0] and self.headC == getFood[1]:
                    self.score = self.score + 1
                    self.snakeLen = self.snakeLen + 1
                    self.snake.append([self.headR, self.headC])
                    self.food.popleft()
                else:
                    self.snake.popleft()
                    if [self.headR, self.headC] in self.snake:
                        return -1
                    self.snake.append([self.headR, self.headC])

            else:
                self.snake.popleft()
                if [self.headR, self.headC] in self.snake:
                    return -1
                self.snake.append([self.headR, self.headC])


            return self.score
        else:
            return -1


obj = SnakeGame(3, 3, [[2, 0], [0,0], [0, 2], [0, 1],[2,2],[0,1]])
print(obj.move("D"))
print(obj.move("D"))
print(obj.move("R"))
print(obj.move("U"))
print(obj.move("U"))
print(obj.move("L"))
print(obj.move("D"))
print(obj.move("R"))
print(obj.move("R"))
print(obj.move("U"))
print(obj.move("L"))
print(obj.move("L"))
print(obj.move("D"))
print(obj.move("R"))
print(obj.move("U"))

