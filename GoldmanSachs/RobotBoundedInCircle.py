instructions= "GL"
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # check for two condition to see if the robot is in circle or not
        # robot is in circle if one of these two conditions are true
        # first if for a given set of direction if the starting point and the ending point is same
        # second if the direction of the robot is not North

        # first check if the robot is moving in a right or left direction or not? or its just moving in just one direction
        if "L" not in instructions and "R" not in instructions:
            return False
        else:
            # x and y is the starting coordinates of the robot
            # dir is the direction of the robot
            # initially the robot is facing right direction
            x=0
            y=0
            dir= 0
            moves= [[0, 1], [1, 0], [0,-1], [-1, 0]]
            # North =0
            # East = 1
            # South= 2
            # West= 3

            for ins in instructions:
                if ins == 'G':
                    #robot will move forward by + 1 step in whichever direction it is
                    x = x + moves[dir][0]
                    y = y + moves[dir][1]
                elif ins == 'L':
                    dir = (dir + 3) % 4
                elif ins == 'R':
                    dir = (dir + 1) % 4

            circle = True if x==0 and y==0 or dir !=0 else False
            return circle

obj=Solution()
print(obj.isRobotBounded(instructions))