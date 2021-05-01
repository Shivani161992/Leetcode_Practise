from typing import List
h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        hbreadth= 0
        prev=0
        for h in horizontalCuts:
            height= h-prev
            hbreadth= max(height, hbreadth)
            prev= h

        prev=0
        vlength=0
        for v in verticalCuts:
            height= v-prev
            vlength= max(vlength, height)
            prev=v

        maxarea= (hbreadth * vlength) % ((10**9) + 7)
        return maxarea

obj=Solution()
print(obj.maxArea(h, w, horizontalCuts, verticalCuts))
