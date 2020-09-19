from typing import List
asteroids= [1,-2,-2,-2]
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack= [asteroids[0]]
        index = 1
        while index < len(asteroids):
            get = stack[len(stack) - 1]
            if (get > 0  and asteroids[index] > 0) or (get < 0  and asteroids[index] < 0):
                stack.append(asteroids[index])
                index = index + 1
            elif get > 0  and asteroids[index] < 0:
                if get == abs(asteroids[index]):
                    stack.pop()
                    index = index + 1
                    if len(stack) == 0:
                        if index < len(asteroids):
                            stack.append(asteroids[index])
                            index= index +1
                elif get > abs(asteroids[index]):
                    index= index +1
                elif get < abs(asteroids[index]):
                    stack.pop()
                    if len(stack) == 0:
                        if index < len(asteroids):
                            stack.append(asteroids[index])
                            index = index + 1
            elif get < 0 and asteroids[index] > 0 :
                stack.append(asteroids[index])
                index = index + 1

        return stack



obj=Solution()
print(obj.asteroidCollision(asteroids))
