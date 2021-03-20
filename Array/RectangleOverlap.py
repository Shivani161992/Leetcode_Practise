rec1 = [0,0,1,1]
rec2 = [2,2,3,3]
from typing import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rectangle1= [[rec1[0], rec1[1]], [rec1[0], rec1[3]], [rec1[2], rec1[1]], [rec1[2], rec1[3]]]
        rectangle2 = [[rec2[0], rec2[1]], [rec2[0], rec2[3]], [rec2[2], rec2[1]], [rec2[2], rec2[3]]]

        for point in rectangle2:
            recx= point[0]
            recy= point[1]
            if ((recx > rectangle1[0][0] and recy > rectangle1[0][1]) and (recx > rectangle1[1][0] and recy < rectangle1[1][1]) and (recx < rectangle1[2][0] and recy > rectangle1[2][1]) and (recx < rectangle1[3][0] and recy < rectangle1[3][1])):
                return True
            elif ((recx > rectangle1[0][0] and recy >= rectangle1[0][1]) and (recx > rectangle1[1][0] and recy < rectangle1[1][1]) and (recx < rectangle1[2][0] and recy >= rectangle1[2][1]) and (recx < rectangle1[3][0] and recy < rectangle1[3][1])):
                return True
        return False



obj = Solution()
print(obj.isRectangleOverlap(rec1, rec2))