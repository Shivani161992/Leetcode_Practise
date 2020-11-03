from typing import List
height = [0,1,0,2,1,0,1,3,2,1,2,1]
class Solution:
    def trap_bruteforce(self, height: List[int]) -> int:
        total_water = 0
        if len(height) < 2:
            return total_water

        #calculate total water
        for i in range(0, len(height)):
            lmax = max(height[:i + 1])
            rmax = max(height[i:])
            water_building= min(lmax, rmax)
            hwater= water_building - height[i]
            total_water= total_water + hwater
        return total_water

    def trap_dynaminprogramming(self, height: List[int]) -> int:
        total_water = 0
        if len(height) < 2:
            return total_water

        # pre calculate lmax for all the values
        lmax = [None] * len(height)
        lmax[0] = height[0]
        for i in range(1, len(lmax)):
            lmax[i] = max(height[i], lmax[i - 1])

        # pre calculate rmax for all the values
        rmax = [None] * len(height)
        rmax[len(lmax) - 1] = height[len(lmax) - 1]
        for i in range(len(lmax) - 2, -1, -1):
            rmax[i] = max(height[i], rmax[i + 1])

        # calculate total water
        for i in range(0, len(height)):
            water_building = min(lmax[i], rmax[i])
            hwater = water_building - height[i]
            total_water = total_water + hwater
        return total_water


    def trap(self, height: List[int]) -> int:
        twater = 0
        if len(height) < 2:
            return twater

        i=0
        j= len(height)-1
        lmax=height[i]
        rmax=height[j]
        twater=0
        while i != j:
            if lmax <= rmax:
                building_water= lmax- height[i]
                i = i + 1
                lmax= max(lmax, height[i])
            elif rmax < lmax:
                building_water = rmax - height[j]
                j = j - 1
                rmax = max(rmax, height[j])

            twater = twater + building_water
        return twater






obj=Solution()
print(obj.trap(height))
